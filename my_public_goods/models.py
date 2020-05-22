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


author = 'Satarupa'

doc = """
This is a public good game 
"""


class Constants(BaseConstants):
    name_in_url = 'my_public_goods'
    players_per_group = 2
    num_rounds = 2
    endowment = c(100)
    multiplier = 2
    Showup_fee = 50


class Subsession(BaseSubsession):
    pass


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
            print('round_number:', p.round_number)
            print('all round data', [s.payoff for s in p.in_all_rounds() ])
            print('num_rounds', Constants.num_rounds)
            if Constants.num_rounds == self.round_number:
                p.set_round_payoff()
                p.set_showup_fee()


            ### uncomment this if you need random payoff
            # if Constants.num_rounds == self.round_number:
            #     p.set_random_payoff()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = "how much are you willing to contribute?"
    )
    rounds_payoff = models.CurrencyField()
    final_payoff = models.CurrencyField()
    print('players')
    current_round_number = models.CurrencyField()
    def set_round_payoff(self):
        # print('set_round_payoff')
        # print(self)
        # self.current_round_number = self.round_nummber
        self.rounds_payoff = 0
        for ar in self.in_all_rounds():
            if ar.round_number % 2 == 0:
                self.rounds_payoff += ar.payoff
        return self.rounds_payoff

    def set_showup_fee(self):
        self.final_payoff = self.rounds_payoff + Constants.Showup_fee
        return self.final_payoff


    ### uncomment this for random round payoff
    # def set_random_payoff(self):
    #     print('set_random_payoff')
    #     import random
    #     self.random_payoff = random.choice(self.in_all_rounds()).payoff
    #     return self.random_payoff






