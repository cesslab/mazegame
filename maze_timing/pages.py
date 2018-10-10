from ._builtin import Page
from .models import Constants


class InstructionPage(Page):
    def vars_for_template(self):
        maze_game = Constants.maze_game
        return {
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


maze_page_sequence = [MazePage]*Constants.num_rounds

page_sequence = [InstructionPage] + maze_page_sequence
