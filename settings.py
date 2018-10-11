from os import environ

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
       'name': 'maze_timing',
       'display_name': "Maze Timing",
       'num_demo_participants': 1,
       'app_sequence': ['maze_timing'],
        'seconds_to_solve_maze': 250,
    },
]

LANGUAGE_CODE = 'en'

REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'

ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'w#cow6oqpw5n$e#3k8dm0fypnwfd0rp2@tb_2_q$z0s-e0n7-n'

INSTALLED_APPS = ['otree']
