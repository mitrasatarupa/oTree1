from .models import Slider
from slider_task.pages import SliderTaskPage
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Guess(Page):
    form_model = 'player'
    form_fields = ['guess']
    timeout_seconds = 10


class ResultsWaitPage(WaitPage):
    pass
    # after_all_players_arrive = "prepare_sliders"

class Results(Page):
    pass

class Sliders(SliderTaskPage):
    Constants = Constants
    Slider = Slider

page_sequence = [Guess, ResultsWaitPage, Sliders, Results]
