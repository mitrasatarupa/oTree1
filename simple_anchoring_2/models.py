from otree.db.models import ForeignKey
from slider_task.models import BaseSlider, SliderPlayer
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
    name_in_url = 'simple_anchoring'
    players_per_group = None
    num_rounds = 1
    sequence_ascending = " 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 = ??? "
    sequence_descending = " 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = ???"
    print(sequence_ascending)
    print(sequence_descending)
    slider_columns = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            import random
            p.ascending = random.choice([True,False])
            p.prepare_sliders(num=20, min=0, max=4)



class Group(BaseGroup):
    avg_ascending = models.FloatField()
    avg_decending = models.FloatField()
    num_ascenders = models.IntegerField()
    num_descenders = models.IntegerField()


    def set_payoffs(self):
        players = self.get_players()
        guesses = [p.guess for p in players]
        ascenders = [p for p in players if p.ascending == True]
        descenders = [p for p in players if p.ascending == False]


        for p in players:
            if p.ascending == True:
                avg_ascending = sum(guesses)/len(ascenders)
                print(avg_ascending)
            else:
                avg_descending = sum(guesses)/len(descenders)
                print(avg_descending)


class Player(SliderPlayer):
    ascending = models.BooleanField()
    guess = models.IntegerField(label = "Please enter a quick approximate guess of the answer")

class Slider(BaseSlider):
    player = ForeignKey(Player, on_delete=models.CASCADE)