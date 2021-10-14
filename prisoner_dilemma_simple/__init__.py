from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner_dilemma_simple'
    players_per_group = 2
    num_rounds = 1
    both_cooperate = -1
    both_defect = -3
    onecooperate_otherdefect_high = 0
    onecooperate_otherdefect_low = -4

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #input decision variable
    defect = models.BooleanField(
        label="Please indicate if you want to cooperate or defect",
        choices=[
            [True,"Defect"],
            [False, "Cooperate"],
        ]
    )


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = ["defect"]

# because the game is interactive qe need all players to arrive first
class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group:Group):
        player_lists = group.get_players()
        player_1 = player_lists[0]
        player_2 = player_lists[1]
        if player_1.defect:
            if player_2.defect:
                player_1.payoff = Constants.both_defect
                player_2.payoff = Constants.both_defect
            else:
                player_1.payoff = Constants.onecooperate_otherdefect_high
                player_2.payoff = Constants.onecooperate_otherdefect_low
        else:
            if player_2.defect:
                player_1.payoff = Constants.onecooperate_otherdefect_low
                player_2.payoff = Constants.onecooperate_otherdefect_high
            else:
                player_1.payoff = Constants.both_cooperate
                player_2.payoff = Constants.both_cooperate


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
