from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Guess(Page):
    form_model = 'player'
    form_fields = ['guess']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'



class Results(Page):

    def vars_for_template(self):
        sorted_guesses = sorted(p.guess for p in self.group.get_players())
        return dict(sorted_guesses=sorted_guesses)

        # players = self.player.in_all_rounds()
        #
        # return dict(
        #     Guesses = [p.Guess for p in players],
        #     total_guess = sum(Guesses),
        #     two_third_average = 2/3 * self.total_guess,
        # )





page_sequence = [Introduction, Guess, ResultsWaitPage, Results]
