from os import environ

SESSION_CONFIGS = [
    dict(
         name='multiply_app',
         app_sequence=['multiply_app'],
         display_name="Multiply App",
         num_demo_participants=3,
     ),
    dict(
        name='real_effort_numbers',
        app_sequence=['real_effort_numbers'],
        display_name="Add up two numbers",
        num_demo_participants=3,
    ),
    dict(
        name='prisoner_dilemma_simple',
        app_sequence=['prisoner_dilemma_simple'],
        display_name="Prisoner Dilemma Simple Version",
        num_demo_participants=4,
    ),
    dict(
         name='interruption_research',
         app_sequence=['interruption_research'],
         display_name="Interruption Research",
         num_demo_participants=1,
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '7275890819337'
