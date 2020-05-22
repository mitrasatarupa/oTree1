from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Consent(Page):
    form_model = 'player'
    form_fields = ['Play_Game']


class Contribute(Page):
    form_model = 'player'
    form_fields = ['Play_Game','contribution']



class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    def vars_for_template(self):
        return dict(total_earnings=self.group.total_contribution * Constants.multiplier)
        # total_round_payoff = [p.set_round_payoff for p in self.player.set_round_payoff()])



page_sequence = [Consent, Contribute, ResultsWaitPage, Results]
