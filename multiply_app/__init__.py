from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'multiply_app'
    players_per_group = None
    num_rounds = 1
    factor = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number_entered = models.FloatField()


# PAGES
class MyPage(Page):
    form_model ="player"
    #This a list in []
    form_fields=["number_entered"]

#wait page is deleted as we dont want participants for everyone to enter
#class ResultsWaitPage(WaitPage):
# pass

class Results(Page):
    #this tells pycharm to highlight otree commands
    @staticmethod
    #defining special function that connects to html vars for template
    def vars_for_template(player:Player):
        #usa propiedeades del metodo player y del metodo factor
        result=player.number_entered*Constants.factor
        return{
            "resultsz":result
        }


page_sequence = [MyPage, Results]
