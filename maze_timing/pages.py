from ._builtin import Page
from .models import Constants


class MazePage(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds']

    def vars_for_template(self):
        return {
            'seconds_to_solve': self.session.config['seconds_to_solve_maze_1']
        }


page_sequence = [
    MazePage,
]
