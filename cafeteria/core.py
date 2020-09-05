import random
import collections
import matplotlib.pyplot as plt


SHOW_MEMBER = 10
MAX_MEMBER = 7
OUT_TIME = 20
SEED = 42

SIT_SCORE = 100
PENALTY_SCORE = [-20, -30, -10, -40, -50]


class Cafeteria:

    def __init__(self, data, time):
        self.table = data[0]
        self.number = data[1]
        self.seats = data[2]

        random.seed(SEED)
        self.group_member = collections.deque([random.randint(1, MAX_MEMBER) for _ in range(SHOW_MEMBER)])
        self.score = [0] * (time + 1)
        self.flag = 0
        self.index = 0

    def make_next_group(self):
        self.group_member.popleft()
        self.group_member.append(random.randint(1, MAX_MEMBER))
        for y in range(self.table):
            for x in range(self.number[y]):
                if self.seats[y][x] != -1:
                    self.seats[y][x] += 1
                    if self.seats[y][x] == OUT_TIME:
                        self.seats[y][x] = 0
