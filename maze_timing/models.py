from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

from experiment.maze_game import MazeCollection, Participant


class Constants(BaseConstants):
    name_in_url = 'maze_timing'
    players_per_group = None
    num_rounds = 35
    INSTRUCTIONS_ROUND = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for player in self.get_players():
                Participant.set_maze_collection(player, MazeCollection())


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    solved = models.IntegerField(default=0)
    solve_time_seconds = models.IntegerField()
    maze_id = models.CharField(max_length=255)
