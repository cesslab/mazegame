import random
from typing import List


class Maze:
    def __init__(self, name: str, start_x: int, start_y: int, end_x: int, end_y: int):
        self.name = name
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y


class MazeCollection:
    def __init__(self):
        self.mazes = [
            Maze('easy1', 147, 2, 169, 314),
            Maze('easy2', 147, 2, 169, 314),
            Maze('easy3', 147, 2, 169, 314),
            Maze('easyM1', 147, 2, 169, 314),
            Maze('easyM2', 147, 2, 169, 314),
            Maze('easyM3', 147, 2, 169, 314),
            Maze('hard1', 147, 2, 169, 314),
            Maze('hard2', 147, 2, 169, 314),
            Maze('hard3', 147, 2, 169, 314),
            Maze('hardV1', 147, 2, 169, 314),
            Maze('hardV2', 147, 2, 169, 314),
            Maze('hardV3', 147, 2, 169, 314),
            Maze('medium1', 147, 2, 169, 314),
            Maze('medium2', 147, 2, 169, 314),
            Maze('medium3', 147, 2, 169, 314)]
        random.shuffle(self.mazes)

        self.rounds = len(self.mazes)

    def maze(self, round_number: int) -> Maze:
        return self.mazes[round_number - 1]

    def num_mazes(self) -> int:
        return len(self.mazes)

    def maze_ids(self) -> List[str]:
        return [maze.name for maze in self.mazes]


class Participant:
    @staticmethod
    def get_maze_collection(player) -> MazeCollection:
        return player.participant.vars['maze_collection']

    @staticmethod
    def set_maze_collection(player, maze_collection: MazeCollection):
        player.participant.vars['maze_collection'] = maze_collection
