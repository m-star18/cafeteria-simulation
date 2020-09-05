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
    """
    食堂のシミュレーションライブラリ

    Attributes
    ----------
    self.table: int
        食堂のテーブルの数。
    self.number: list of int
        テーブル毎の席の数。
    self.seats: list of int
        席の状態をintで管理している配列。
    self.group_member: collections.deque of int
        10ターン後までに来るグループの人数。
    self.score: list of int
        各ターンのシミュレーションの合計スコア。
    self.flag: int
        現在のターンで座れた人数。
    self.index: int
        現在のターン。
    """

    def __init__(self, data, time):
        """
        Parameters
        ----------
        data: list
            食堂のデータ。
            data[0]: int
                食堂のテーブルの数。
            data[1]: list of int
                食堂のテーブル毎の席の数。
            data[2]: list of int
                席の状態をintで管理している配列。
        time: int
            シミュレーションを行う時間

        Notes
        -----
        self.seatsにある値について
        -1 -> 空席
        n -> 直近nターンで埋まった席
        """
        self.table = data[0]
        self.number = data[1]
        self.seats = data[2]

        random.seed(SEED)
        self.group_member = collections.deque([random.randint(1, MAX_MEMBER) for _ in range(SHOW_MEMBER)])
        self.score = [0] * (time + 1)
        self.flag = 0
        self.index = 0

    def make_next_group(self):
        """
        次のターンの状態を追加する。
        """
        self.group_member.popleft()
        self.group_member.append(random.randint(1, MAX_MEMBER))
        for y in range(self.table):
            for x in range(self.number[y]):
                if self.seats[y][x] != -1:
                    self.seats[y][x] += 1
                    if self.seats[y][x] == OUT_TIME:
                        self.seats[y][x] = 0

    def penalty(self):
        """
        毎ターンのペナルティを計算する。

        Parameter
        ----------
        penalty1_flag: list of bool
            ペナルティ1のフラグ。
        penalty3_count: int
            探索積みの人数をカウント。
        penalty3_flag: int
            ペナルティ3のフラグ。
        penalty4_flag: bool
            ペナルティ4のフラグ。

        Notes
        -----
        ペナルティ1
            -20点
            他の席が空いているのに知らない人が隣りに座ってきた場合。
        ペナルティ2
            -30点
            奇数グループの対面に相手が座った場合。
        ペナルティ3
            -10点
            グループの人数を分けた場合。
        ペナルティ4
            -40点
            ペナルティ3において分割しすぎてしまい、孤食が出た場合。
        ペナルティ5
            -50点
            人が座れていなかった場合。
        """
        penalty1_flag = [False, False]
        penalty3_count = 0
        penalty3_flag = 0
        penalty4_flag = True

        for y in range(self.table):
            # ペナルティ1
            if all(self.seats[y][x] == -1 for x in range(self.number[y])):
                penalty1_flag[1] = True

            for x in range(self.number[y]):
                if self.seats[y][x] != 0:
                    continue

                # ペナルティ2
                if x % 2 == 0 and self.seats[y][x + 1] != -1 and self.seats[y][x] != self.seats[y][x + 1]:
                    penalty1_flag[0] = True
                    self.score[self.index] += PENALTY_SCORE[1]

                # ペナルティ4
                if x > 0:
                    if x > 1:
                        if self.seats[y][x - 2] == self.seats[y][x]:
                            penalty4_flag = False
                    if self.seats[y][x - 1] == self.seats[y][x]:
                        penalty4_flag = False

                if x + 1 < self.number[y]:
                    if x + 2 < self.number[y]:
                        if self.seats[y][x + 2] == self.seats[y][x]:
                            penalty4_flag = False
                    # ペナルティ3
                    if self.seats[y][x + 1] == self.seats[y][x]:
                        penalty3_count += 1
                        penalty4_flag = False
                    else:
                        if penalty3_count != self.number[y]:
                            penalty3_flag += 1

                self.score[self.index] += penalty3_flag * PENALTY_SCORE[2]

                if penalty4_flag:
                    self.score[self.index] += PENALTY_SCORE[3]

        if all(penalty1_flag):
            self.score[self.index] += PENALTY_SCORE[0]

        # ペナルティ5
        if self.group_member[0] == self.flag:
            self.make_next_group()
        else:
            self.group_member[0] -= self.flag
            self.score[self.index] += self.group_member[0] * PENALTY_SCORE[4]

        self.flag = 0

    def run(self, group):
        """
        シミュレーションを実行する。

        Parameters
        ----------
        group: list of list
            食堂のデータ。
        """
        if len(group) > self.group_member[0]:
            print('1ターンに来る人を指定する上限を超えています。')
            exit()

        self.index += 1
        for place in group:
            if self.seats[place[0]][place[1]] == -1:
                self.seats[place[0]][place[1]] = 0
                self.score[self.index] += SIT_SCORE
                self.flag += 1

        self.penalty()
        self.score[self.index] += self.score[self.index - 1]

    def show(self):
        plt.plot(range(self.index + 1), self.score)
        plt.title("total score")
        plt.xlabel("time")
        plt.ylabel("score")
        plt.grid(True)
        plt.show()
