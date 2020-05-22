
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Guess(Page):
    form_model = 'player'
    form_fields = ['guess']
    timeout_seconds = 30


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Result(Page):
    pass



page_sequence = [Guess, ResultsWaitPage,Result]
