# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random




# </standard imports>



author = 'Curtis Kephart (economicurtis@gmail.com)'

doc = """
Real Effort Task. Type as many strings as possible.  
"""

class Constants(BaseConstants):
    name_in_url = 'task_typing'
    players_per_group = None
    num_rounds = 10 # must be more than the max one person can do in task_timer seconds


    reference_texts = [
        'Y90ZQ4gF',
        'WSx7IJ8Y',
        '6gt6k1dZ',
        '8gkmGZY3',
        'tz4hJ6Nq',
        'SY3BOD9c',
        'FAojzXfs',
        '7Hoep0BQ',
        'TXVUwqGN',
        'Ig6hl84v',
    ]

class Subsession(BaseSubsession):

    def before_session_starts(self):

        players = self.get_players()


        for p in self.get_players():
            p.correct_text = Constants.reference_texts[self.round_number - 1]

class Group(BaseGroup):
	pass

class Player(BasePlayer):

    def score_round(self):
        # update player payoffs
        if (self.correct_text == self.user_text):
            self.is_correct = True
            self.payoff_score = 1
        else: 
            self.is_correct = False
            self.payoff_score = c(0)      




    correct_text = models.CharField(
        doc="user's transcribed text")

    user_text = models.CharField(
        doc="user's transcribed text",
        widget=widgets.TextInput(attrs={'autocomplete':'off'}))

    is_correct = models.BooleanField(
        doc="did the user get the task correct?")

    ret_final_score = models.IntegerField(
        doc="player's total score up to this round")

    payoff_score = models.CurrencyField(
            doc = '''score in this task'''
        )
