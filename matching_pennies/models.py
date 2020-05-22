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


doc = """
A demo of how rounds work in oTree, in the context of 'matching pennies'
"""


class Constants(BaseConstants):
    name_in_url = 'matching_pennies'
    players_per_group = 2
    num_rounds = 5
    stakes = c(100) # this is new. perhaps stakes is something associated with winning or losing amount


class Subsession(BaseSubsession):
    def creating_session(self):
        import random

        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round # so this line of code saves the previously generated random round in a dictionary called paying round which can be retrieved later using this name.
        if self.round_number == 3:
            # reverse the roles
            matrix = self.get_group_matrix()
            print(self.get_group_matrix())
            # supppose we are playing with 4 participants this will show up as:
            # [[<Player  1>, <Player  2>],
            #  [<Player  3>, <Player  4>]]
            # this in a group of two, 1 and 2 are forming group and 3 and 4 are group and their roles as defined in def(role) are
            # as per their group id i.e.  "id 1" = 1st element in the matrix.
            for row in matrix:
                row.reverse()
            self.set_group_matrix(matrix)
            # on reversing the rows of the matrix, it shows up as
            # [[<Player  2>, <Player  1>],
            # [<Player  4>, <Player  3>]]
            print(self.get_group_matrix())
        if self.round_number > 3:
            self.group_like_round(3)


class Group(BaseGroup):
    def set_payoffs(self):
        matcher = self.get_player_by_role('Matcher')
        mismatcher = self.get_player_by_role('Mismatcher')

        if matcher.penny_side == mismatcher.penny_side:
            matcher.is_winner = True
            mismatcher.is_winner = False
        else:
            matcher.is_winner = False
            mismatcher.is_winner = True
        for player in [mismatcher, matcher]:
            if (
                self.subsession.round_number == self.session.vars['paying_round']
                and player.is_winner
            ):
                player.payoff = Constants.stakes
            else:
                player.payoff = c(0)


class Player(BasePlayer):
    penny_side = models.StringField(
        choices=[['Heads', 'Heads'], ['Tails', 'Tails']], widget=widgets.RadioSelect
    )

    is_winner = models.BooleanField()

    def role(self):
        if self.id_in_group == 1:
            return 'Mismatcher'
        if self.id_in_group == 2:
            return 'Matcher'
