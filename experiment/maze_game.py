import random


class Maze:
    def __init__(self, name: str, start_x: int, start_y: int, end_x: int, end_y: int):
        self.name = name
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y


class MazeGame:
    def __init__(self):
        self.mazes = [
            Maze('easy1-100-1', 147, 2, 169, 314),
            Maze('easy2-100-1', 147, 2, 169, 314),
            Maze('easy3-100-1', 147, 2, 169, 314),
            Maze('easyM1-100-20', 147, 2, 169, 314),
            Maze('easyM2-100-20', 147, 2, 169, 314),
            Maze('easyM3-100-20', 147, 2, 169, 314),
            Maze('hard1-60-40', 147, 2, 169, 314),
            Maze('hard2-60-40', 147, 2, 169, 314),
            Maze('hard3-60-40', 147, 2, 169, 314),
            Maze('hardV1-40-60', 147, 2, 169, 314),
            Maze('hardV2-40-60', 147, 2, 169, 314),
            Maze('hardV3-40-60', 147, 2, 169, 314),
            Maze('medium1-100-40', 147, 2, 169, 314),
            Maze('medium2-100-40', 147, 2, 169, 314),
            Maze('medium3-100-40', 147, 2, 169, 314)]
        random.shuffle(self.mazes)

        self.rounds = len(self.mazes)

    def maze(self, round_number: int) -> Maze:
        return self.mazes[round_number]

    def num_mazes(self) -> int:
        return len(self.mazes)

