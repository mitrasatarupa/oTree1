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
    name_in_url = 'new_guess_two_third'
    players_per_group = None
    num_rounds = 3
    guess_max = 100
    jackpot = c(100)

    Instruction_template = 'new_guess_two_third/Instruction.html'




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    two_thirds_avg = models.FloatField()
    best_guess = models.IntegerField()
    num_winners = models.IntegerField()

    def set_payoffs(self):
        players = self.get_players()
        guesses = [p.guess for p in players]
        print(guesses)
        two_thirds_avg = (2 / 3) * sum(guesses) / len(players)
        self.two_thirds_avg = round(two_thirds_avg, 2)
        self.best_guess = min(
            guesses, key=lambda guess: abs(guess - self.two_thirds_avg)
        )
        winners = [p for p in players if p.guess == self.best_guess]
        self.num_winners = len(winners)

        for p in winners:
            p.is_winner = True # note this is not a condition for for loop, in this line of code i m assigning the tag is.winner true to the selected winners
            p.payoff = Constants.jackpot / self.num_winners

    def two_thirds_avg_history(self):
        return [k.two_thirds_avg for k in self.in_previous_rounds()]




class Player(BasePlayer):

    guess = models.IntegerField(
        min=0,
        max=100,
        label = "Please pick a number from 0 to 100"
    )
    is_winner = models.BooleanField()



# def set_payoffs(self):
#         players = self.get_players()
#         Guesses = [p.Guess for p in players]
#         self.total_guess = sum(Guesses)
#         self.two_third_average = 2/3 * self.total_guess
#
#         print('total_guess:', p.total_guess)
#         print('two_third_average:', p.two_third_average)

