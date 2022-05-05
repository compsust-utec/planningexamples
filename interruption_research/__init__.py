from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'interruption_research'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    b_quiz_1 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='1. Me siento calmado'
    )
    
    b_quiz_2 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='2. Me siento seguro'
    )

    b_quiz_3 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='3. Estoy Tenso'
    )

    b_quiz_4 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='4. Estoy contrariado'
    )

    b_quiz_5 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='5. Me siento cómodo (estoy a gusto)'
    )

    b_quiz_6 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='6. Me siento alterado'
    )

    b_quiz_7 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='7. Estoy preocupado ahora por posibles desgracias futuras'
    )

    b_quiz_8 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='8. Me siento descansado'
    )

    b_quiz_9 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='9. Me siento angustiado'
    )

    b_quiz_10 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='10. Me siento confortable'
    )

    b_quiz_11 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='11. Tengo confianza en mi mismo'
    )

    b_quiz_12 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='12. Me siento nervioso'
    )

    b_quiz_13 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='13. Estoy desasosegado'
    )

    b_quiz_14 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='14. Me siento muy “atado” (como oprimido)'
    )

    b_quiz_15 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='15. Estoy relajado'
    )

    b_quiz_16 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='16. Me siento satisfecho'
    )

    b_quiz_17 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='17. Estoy preocupado'
    )

    b_quiz_18 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='18. Me siento aturdido y sobreexcitado'
    )

    b_quiz_19 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='19. Me siento alegre'
    )

    b_quiz_20 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='20. En este momento me siento bien'
    )

    b_quiz_21 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='21. Me siento bien'
    )
    
    b_quiz_22 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='22. Me canso rápidamente'
    )

    b_quiz_23 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='23. Siento ganas de llorar'
    )

    b_quiz_24 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='24. Me gustaría ser tan feliz como otros'
    )

    b_quiz_25 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='25. Pierdo oportunidades por no decidirme pronto'
    )

    b_quiz_26 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='26. Me siento descansado'
    )

    b_quiz_27 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='27. Soy una persona tranquila, serena y sosegada'
    )

    b_quiz_28 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='28. Veo que las dificultades se amontonan y no puedo con ellas'
    )

    b_quiz_29 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='29. Me preocupo demasiado por cosas sin importancia'
    )

    b_quiz_30 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='30. Soy feliz'
    )

    b_quiz_31 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='31. Suelo tomar las cosas demasiado seriamente'
    )

    b_quiz_32 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='32. Me falta confianza en mí mismo'
    )

    b_quiz_33 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='33. Me siento seguro'
    )

    b_quiz_34 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='34. No suelo afrontar las crisis o dificultades'
    )

    b_quiz_35 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='35. Me siento triste (melancólico)'
    )

    b_quiz_36 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='36. Estoy satisfecho'
    )

    b_quiz_37 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='37. Me rondan y molestan pensamientos sin importancia'
    )

    b_quiz_38 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='38. Me afectan tanto los desengaños, que no puedo olvidarlos'
    )

    b_quiz_39 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='39. Soy una persona estable'
    )

    b_quiz_40 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='40. Cuando pienso sobre asuntos y preocupaciones actuales, me pongo tenso y agitado'
    )


    e_quiz_1 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='1. Me siento calmado'
    )
    
    e_quiz_2 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='2. Me siento seguro'
    )

    e_quiz_3 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='3. Estoy Tenso'
    )

    e_quiz_4 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='4. Estoy contrariado'
    )

    e_quiz_5 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='5. Me siento cómodo (estoy a gusto)'
    )

    e_quiz_6 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='6. Me siento alterado'
    )

    e_quiz_7 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='7. Estoy preocupado ahora por posibles desgracias futuras'
    )

    e_quiz_8 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='8. Me siento descansado'
    )

    e_quiz_9 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='9. Me siento angustiado'
    )

    e_quiz_10 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='10. Me siento confortable'
    )

    e_quiz_11 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='11. Tengo confianza en mi mismo'
    )

    e_quiz_12 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='12. Me siento nervioso'
    )

    e_quiz_13 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='13. Estoy desasosegado'
    )

    e_quiz_14 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='14. Me siento muy “atado” (como oprimido)'
    )

    e_quiz_15 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='15. Estoy relajado'
    )

    e_quiz_16 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='16. Me siento satisfecho'
    )

    e_quiz_17 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='17. Estoy preocupado'
    )

    e_quiz_18 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='18. Me siento aturdido y sobreexcitado'
    )

    e_quiz_19 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='19. Me siento alegre'
    )

    e_quiz_20 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='20. En este momento me siento bien'
    )

    e_quiz_21 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='21. Me siento bien'
    )
    
    e_quiz_22 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='22. Me canso rápidamente'
    )

    e_quiz_23 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='23. Siento ganas de llorar'
    )

    e_quiz_24 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='24. Me gustaría ser tan feliz como otros'
    )

    e_quiz_25 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='25. Pierdo oportunidades por no decidirme pronto'
    )

    e_quiz_26 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='26. Me siento descansado'
    )

    e_quiz_27 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='27. Soy una persona tranquila, serena y sosegada'
    )

    e_quiz_28 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='28. Veo que las dificultades se amontonan y no puedo con ellas'
    )

    e_quiz_29 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='29. Me preocupo demasiado por cosas sin importancia'
    )

    e_quiz_30 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='30. Soy feliz'
    )

    e_quiz_31 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='31. Suelo tomar las cosas demasiado seriamente'
    )

    e_quiz_32 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='32. Me falta confianza en mí mismo'
    )

    e_quiz_33 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='33. Me siento seguro'
    )

    e_quiz_34 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='34. No suelo afrontar las crisis o dificultades'
    )

    e_quiz_35 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='35. Me siento triste (melancólico)'
    )

    e_quiz_36 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='36. Estoy satisfecho'
    )

    e_quiz_37 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='37. Me rondan y molestan pensamientos sin importancia'
    )

    e_quiz_38 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='38. Me afectan tanto los desengaños, que no puedo olvidarlos'
    )

    e_quiz_39 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='39. Soy una persona estable'
    )

    e_quiz_40 = models.IntegerField(
        choices=[[0, '0'], [1, '1'], [2, '2'], [3, '3']],
        widget=widgets.RadioSelect,
        label='40. Cuando pienso sobre asuntos y preocupaciones actuales, me pongo tenso y agitado'
    )


    ## CASE 1

    case_1_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_1_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_1_step_2_name = models.StringField(label='Name')
    case_1_step_2_last_name = models.StringField(label='Last name')
    case_1_step_2_id = models.StringField(label='Code')
    case_1_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_1_step_2_end_date = models.StringField(label='Deadline')
    
    case_1_step_3_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_1_step_4_1 = models.StringField()


    ## CASE 2

    case_2_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_2_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_2_step_2_name = models.StringField(label='Name')
    case_2_step_2_last_name = models.StringField(label='Last name')
    case_2_step_2_id = models.StringField(label='Code')
    case_2_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_2_step_2_end_date = models.StringField(label='Deadline')
    
    case_2_step_3_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_2_step_4_1 = models.StringField()


    ## CASE 3

    case_3_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_3_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_3_step_2_name = models.StringField(label='Name')
    case_3_step_2_last_name = models.StringField(label='Last name')
    case_3_step_2_id = models.StringField(label='Code')
    case_3_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_3_step_2_end_date = models.StringField(label='Deadline')
    
    case_3_step_3_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_3_step_4_1 = models.StringField()


    ## CASE 4

    case_4_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_4_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_4_step_2_name = models.StringField(label='Name')
    case_4_step_2_last_name = models.StringField(label='Last name')
    case_4_step_2_id = models.StringField(label='Code')
    case_4_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_4_step_2_end_date = models.StringField(label='Deadline')
    
    case_4_step_3_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_4_step_4_1 = models.StringField()


    ## CASE 5

    case_5_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_5_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_5_step_2_name = models.StringField(label='Name')
    case_5_step_2_last_name = models.StringField(label='Last name')
    case_5_step_2_id = models.StringField(label='Code')
    case_5_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_5_step_2_end_date = models.StringField(label='Deadline')

    case_5_step_3_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_5_step_4_1 = models.StringField()


    ## CASE 6

    case_6_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_6_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_6_step_2_name = models.StringField(label='Name')
    case_6_step_2_last_name = models.StringField(label='Last name')
    case_6_step_2_id = models.StringField(label='Code')
    case_6_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_6_step_2_end_date = models.StringField(label='Deadline')
    
    case_6_step_3_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_6_step_4_1 = models.StringField()


    ## CASE 7

    case_7_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_7_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_7_step_2_name = models.StringField(label='Name')
    case_7_step_2_last_name = models.StringField(label='Last Name')
    case_7_step_2_id = models.StringField(label='Code')
    case_7_step_2_licence_plate = models.StringField(label='License Plate')
    case_7_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_7_step_2_end_date = models.StringField(label='Deadline')

    case_7_step_3_vehicle_owner = models.StringField(label='Vehicle Owner')
    case_7_step_3_driver_fullname = models.StringField(label="Driver's Full Name")
    case_7_step_3_driver_adress = models.StringField(label="Driver's Adress")
    case_7_step_3_licence_plate = models.StringField(label='License Plate')
    
    case_7_step_4_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_7_step_5_1 = models.StringField()



    # CASE 8

    case_8_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_8_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_8_step_2_name = models.StringField(label='Name')
    case_8_step_2_last_name = models.StringField(label='Last Name')
    case_8_step_2_id = models.StringField(label='Code')
    case_8_step_2_licence_plate = models.StringField(label='License Plate')
    case_8_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_8_step_2_end_date = models.StringField(label='Deadline')

    case_8_step_3_vehicle_owner = models.StringField(label='Vehicle Owner')
    case_8_step_3_driver_fullname = models.StringField(label="Driver's Full Name")
    case_8_step_3_driver_adress = models.StringField(label="Driver's Adress")
    case_8_step_3_licence_plate = models.StringField(label='License Plate')
    
    case_8_step_4_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_8_step_5_1 = models.StringField()


    # CASE 9

    case_9_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_9_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_9_step_2_name = models.StringField(label='Name')
    case_9_step_2_last_name = models.StringField(label='Last Name')
    case_9_step_2_id = models.StringField(label='Code')
    case_9_step_2_licence_plate = models.StringField(label='License Plate')
    case_9_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_9_step_2_end_date = models.StringField(label='Deadline')

    case_9_step_3_vehicle_owner = models.StringField(label='Vehicle Owner')
    case_9_step_3_driver_fullname = models.StringField(label="Driver's Full Name")
    case_9_step_3_driver_adress = models.StringField(label="Driver's Adress")
    case_9_step_3_licence_plate = models.StringField(label='License Plate')
    
    case_9_step_4_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_9_step_5_1 = models.StringField()


    # CASE 10

    case_10_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_10_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_10_step_2_name = models.StringField(label='Name')
    case_10_step_2_last_name = models.StringField(label='Last Name')
    case_10_step_2_id = models.StringField(label='Code')
    case_10_step_2_licence_plate = models.StringField(label='License Plate')
    case_10_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_10_step_2_end_date = models.StringField(label='Deadline')

    case_10_step_3_vehicle_owner = models.StringField(label='Vehicle Owner')
    case_10_step_3_driver_fullname = models.StringField(label="Driver's Full Name")
    case_10_step_3_driver_adress = models.StringField(label="Driver's Adress")
    case_10_step_3_licence_plate = models.StringField(label='License Plate')
    
    case_10_step_4_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_10_step_5_1 = models.StringField()


    # CASE 11

    case_11_step_1_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_11_step_1_2 = models.IntegerField(
        choices=[[1, 'Diamond'], [2, 'Gold'], [3, 'Silver'], [4, 'Regular']],
        widget=widgets.RadioSelect
    )

    case_11_step_2_name = models.StringField(label='Name')
    case_11_step_2_last_name = models.StringField(label='Last Name')
    case_11_step_2_id = models.StringField(label='Code')
    case_11_step_2_licence_plate = models.StringField(label='License Plate')
    case_11_step_2_insurance_type = models.StringField(label='Type of insurance')
    case_11_step_2_end_date = models.StringField(label='Deadline')

    case_11_step_3_vehicle_owner = models.StringField(label='Vehicle Owner')
    case_11_step_3_driver_fullname = models.StringField(label="Driver's Full Name")
    case_11_step_3_driver_adress = models.StringField(label="Driver's Adress")
    case_11_step_3_licence_plate = models.StringField(label='License Plate')
    
    case_11_step_4_1 = models.IntegerField(
        choices=[[1, 'Yes'], [2, 'No']],
        widget=widgets.RadioSelectHorizontal
    )

    case_11_step_5_1 = models.StringField()


    ## Completion time

    start_date = models.StringField()
    end_date = models.StringField()

    case_1_complete_time = models.StringField()
    case_2_complete_time = models.StringField()
    case_3_complete_time = models.StringField()
    case_4_complete_time = models.StringField()
    case_5_complete_time = models.StringField()
    case_6_complete_time = models.StringField()
    case_7_complete_time = models.StringField()
    case_8_complete_time = models.StringField()
    case_9_complete_time = models.StringField()
    case_10_complete_time = models.StringField()
    case_11_complete_time = models.StringField()

    case_1_error_count = models.StringField()
    case_2_error_count = models.StringField()
    case_3_error_count = models.StringField()
    case_4_error_count = models.StringField()
    case_5_error_count = models.StringField()
    case_6_error_count = models.StringField()
    case_7_error_count = models.StringField()
    case_8_error_count = models.StringField()
    case_9_error_count = models.StringField()
    case_10_error_count = models.StringField()
    case_11_error_count = models.StringField()

    list_intr_id = models.StringField()
    list_intr_time = models.StringField()
    pass


# PAGES
class Task(Page):    
    timeout_seconds = 60 * 60
    form_model = 'player'
    form_fields = [
        'case_1_step_1_1', 'case_1_step_1_2', 'case_1_step_2_name', 'case_1_step_2_last_name', 'case_1_step_2_id', 'case_1_step_2_insurance_type', 'case_1_step_2_end_date', 'case_1_step_3_1', 'case_1_step_4_1',
        'case_2_step_1_1', 'case_2_step_1_2', 'case_2_step_2_name', 'case_2_step_2_last_name', 'case_2_step_2_id', 'case_2_step_2_insurance_type', 'case_2_step_2_end_date', 'case_2_step_3_1', 'case_2_step_4_1',
        'case_3_step_1_1', 'case_3_step_1_2', 'case_3_step_2_name', 'case_3_step_2_last_name', 'case_3_step_2_id', 'case_3_step_2_insurance_type', 'case_3_step_2_end_date', 'case_3_step_3_1', 'case_3_step_4_1',
        'case_4_step_1_1', 'case_4_step_1_2', 'case_4_step_2_name', 'case_4_step_2_last_name', 'case_4_step_2_id', 'case_4_step_2_insurance_type', 'case_4_step_2_end_date', 'case_4_step_3_1', 'case_4_step_4_1',
        'case_5_step_1_1', 'case_5_step_1_2', 'case_5_step_2_name', 'case_5_step_2_last_name', 'case_5_step_2_id', 'case_5_step_2_insurance_type', 'case_5_step_2_end_date', 'case_5_step_3_1', 'case_5_step_4_1',
        'case_6_step_1_1', 'case_6_step_1_2', 'case_6_step_2_name', 'case_6_step_2_last_name', 'case_6_step_2_id', 'case_6_step_2_insurance_type', 'case_6_step_2_end_date', 'case_6_step_3_1', 'case_6_step_4_1',
        'case_7_step_1_1', 'case_7_step_1_2', 'case_7_step_2_name', 'case_7_step_2_last_name', 'case_7_step_2_id', 'case_7_step_2_licence_plate', 'case_7_step_2_insurance_type', 'case_7_step_2_end_date', 'case_7_step_3_vehicle_owner', 'case_7_step_3_driver_fullname', 'case_7_step_3_driver_adress', 'case_7_step_3_licence_plate', 'case_7_step_4_1', 'case_7_step_5_1',
        'case_8_step_1_1', 'case_8_step_1_2', 'case_8_step_2_name', 'case_8_step_2_last_name', 'case_8_step_2_id', 'case_8_step_2_licence_plate', 'case_8_step_2_insurance_type', 'case_8_step_2_end_date', 'case_8_step_3_vehicle_owner', 'case_8_step_3_driver_fullname', 'case_8_step_3_driver_adress', 'case_8_step_3_licence_plate', 'case_8_step_4_1', 'case_8_step_5_1',
        'case_9_step_1_1', 'case_9_step_1_2', 'case_9_step_2_name', 'case_9_step_2_last_name', 'case_9_step_2_id', 'case_9_step_2_licence_plate', 'case_9_step_2_insurance_type', 'case_9_step_2_end_date', 'case_9_step_3_vehicle_owner', 'case_9_step_3_driver_fullname', 'case_9_step_3_driver_adress', 'case_9_step_3_licence_plate', 'case_9_step_4_1', 'case_9_step_5_1',
        'case_10_step_1_1', 'case_10_step_1_2', 'case_10_step_2_name', 'case_10_step_2_last_name', 'case_10_step_2_id', 'case_10_step_2_licence_plate', 'case_10_step_2_insurance_type', 'case_10_step_2_end_date', 'case_10_step_3_vehicle_owner', 'case_10_step_3_driver_fullname', 'case_10_step_3_driver_adress', 'case_10_step_3_licence_plate', 'case_10_step_4_1', 'case_10_step_5_1',
        'case_11_step_1_1', 'case_11_step_1_2', 'case_11_step_2_name', 'case_11_step_2_last_name', 'case_11_step_2_id', 'case_11_step_2_licence_plate', 'case_11_step_2_insurance_type', 'case_11_step_2_end_date', 'case_11_step_3_vehicle_owner', 'case_11_step_3_driver_fullname', 'case_11_step_3_driver_adress', 'case_11_step_3_licence_plate', 'case_11_step_4_1', 'case_11_step_5_1',
        'case_1_complete_time', 'case_2_complete_time', 'case_3_complete_time', 'case_4_complete_time', 'case_5_complete_time', 'case_6_complete_time', 'case_7_complete_time', 'case_8_complete_time', 'case_9_complete_time', 'case_10_complete_time', 'case_11_complete_time',
        'case_1_error_count', 'case_2_error_count', 'case_3_error_count', 'case_4_error_count', 'case_5_error_count', 'case_6_error_count', 'case_7_error_count', 'case_8_error_count', 'case_9_error_count', 'case_10_error_count', 'case_11_error_count',
        'list_intr_id', 'list_intr_time'
    ]
    
    pass


#class ResultsWaitPage(WaitPage):
#    pass


class BeginQuiz(Page):
    form_model = 'player'
    form_fields = [
        'b_quiz_1', 'b_quiz_2', 'b_quiz_3', 'b_quiz_4', 'b_quiz_5', 'b_quiz_6', 'b_quiz_7', 'b_quiz_8', 'b_quiz_9', 'b_quiz_10',
        'b_quiz_11', 'b_quiz_12', 'b_quiz_13', 'b_quiz_14', 'b_quiz_15', 'b_quiz_16', 'b_quiz_17', 'b_quiz_18', 'b_quiz_19', 'b_quiz_20',
        'b_quiz_21', 'b_quiz_22', 'b_quiz_23', 'b_quiz_24', 'b_quiz_25', 'b_quiz_26', 'b_quiz_27', 'b_quiz_28', 'b_quiz_29', 'b_quiz_30',
        'b_quiz_31', 'b_quiz_32', 'b_quiz_33', 'b_quiz_34', 'b_quiz_35', 'b_quiz_36', 'b_quiz_37', 'b_quiz_38', 'b_quiz_39', 'b_quiz_40'
    ]
    pass

class EndQuiz(Page):
    form_model = 'player'
    form_fields = [
        'e_quiz_1', 'e_quiz_2', 'e_quiz_3', 'e_quiz_4', 'e_quiz_5', 'e_quiz_6', 'e_quiz_7', 'e_quiz_8', 'e_quiz_9', 'e_quiz_10',
        'e_quiz_11', 'e_quiz_12', 'e_quiz_13', 'e_quiz_14', 'e_quiz_15', 'e_quiz_16', 'e_quiz_17', 'e_quiz_18', 'e_quiz_19', 'e_quiz_20',
        'e_quiz_21', 'e_quiz_22', 'e_quiz_23', 'e_quiz_24', 'e_quiz_25', 'e_quiz_26', 'e_quiz_27', 'e_quiz_28', 'e_quiz_29', 'e_quiz_30',
        'e_quiz_31', 'e_quiz_32', 'e_quiz_33', 'e_quiz_34', 'e_quiz_35', 'e_quiz_36', 'e_quiz_37', 'e_quiz_38', 'e_quiz_39', 'e_quiz_40'
    ]
    pass

page_sequence = [Task, EndQuiz] #BeginQuiz
