from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

from experiment.maze_game import MazeGame


class Constants(BaseConstants):
    name_in_url = 'maze_timing'
    players_per_group = None
    maze_game = MazeGame()
    num_rounds = maze_game.rounds


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    solved = models.BooleanField(default=False)
    solve_time_seconds = models.IntegerField()
    maze_id = models.CharField(max_length=255)
