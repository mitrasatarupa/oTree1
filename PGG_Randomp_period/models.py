from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'PGG_Randomp_period'
    players_per_group = 2
    num_rounds = 5
    endowment = c(100)
    multiplier = 2
    Showup_fee = 50


class Subsession(BaseSubsession):
    pass
    # def creating_session(self):
    #     import random
    #     if self.round_number == 1:
    #         paying_round = random.randint(1, Constants.num_rounds)
    #         self.session.vars['paying_round'] = paying_round

class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        print('set_payoffs')
        players = self.get_players()
        contributions = [p.contribution for p in players]
        print('contributions:', contributions)
        self.total_contribution = sum(contributions)
        self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group
        for p in players:
            p.payoff = Constants.endowment - p.contribution + self.individual_share

            if Constants.num_rounds == self.round_number:
                p.set_random_payoff()


class Player(BasePlayer):
        contribution = models.CurrencyField(
            min=0,
            max=Constants.endowment,
            label = "how much are you willing to contribute?"
        )
        random_payoff = models.CurrencyField()
        print('players')
        current_round_number = models.CurrencyField()
        Play_Game = models.StringField(
            choices=[['Yes', 'Yes'], ['No', 'No'] , ['other', 'other']], widget=widgets.RadioSelect
        )
        def set_random_payoff(self):
            print('set_random_payoff')
            import random
            self.random_payoff = random.choice(self.in_all_rounds()).payoff
            return self.random_payoff

