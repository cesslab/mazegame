from ._builtin import Page
from .models import Constants


class InstructionPage(Page):
    def is_displayed(self):
        if self.round_number == Constants.INSTRUCTIONS_ROUND:
            return True
        else:
            return False

    def vars_for_template(self):
        maze_game = Constants.maze_game
        maze_ids = maze_game.maze_ids()
        return {
            'maze_ids': maze_ids,
            'num_mazes': maze_game.num_mazes(),
            'minutes_to_solve': self.session.config['seconds_to_solve_maze']/60,
        }


class MazePage(Page):
    form_model = 'player'
    form_fields = ['solved', 'solve_time_seconds', 'maze_id']

    def vars_for_template(self):
        maze = Constants.maze_game.maze(self.round_number)
        return {
            'seconds_to_solve': self.session.config['seconds_to_solve_maze'],
            'maze_img': 'maze_timing/img/'+maze.name+'.png',
            'maze_id': maze.name,
            'start_x': maze.start_x,
            'start_y': maze.start_y,
            'end_x': maze.end_x,
            'end_y': maze.end_y,
            'round': self.round_number,
        }


page_sequence = [InstructionPage, MazePage]
