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
    # slider_columns = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            import random
            p.ascending = random.choice([True,False])




class Group(BaseGroup):
    avg_ascending = models.FloatField()
    avg_descending = models.FloatField()


    def set_payoffs(self):
        players = self.get_players()
        ascenders = [p for p in players if p.ascending == True]
        print(ascenders)
        descenders = [p for p in players if p.ascending == False]
        ascendGuess = [p.guess for p in ascenders]
        print(ascendGuess)
        descendGuess = [p.guess for p in descenders]

        # for p in players:
        #     if p.ascending == True:
        self.avg_ascending = sum(ascendGuess)/len(ascenders)
        print(sum(ascendGuess))
        print(self.avg_ascending)
            # else:
        self.avg_descending = sum(descendGuess)/len(descenders)
        print(self.avg_descending)




class Player(BasePlayer):
    ascending = models.BooleanField()
    guess = models.IntegerField(label = "Please enter a quick approximate guess of the answer")


