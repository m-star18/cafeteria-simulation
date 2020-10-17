import random
import collections
import matplotlib.pyplot as plt
import datetime
import os


SHOW_MEMBER = 10
MAX_MEMBER = 7
MIN_OUT_TIME = 60
MAX_OUT_TIME = 120
SEED = 42

SIT_SCORE = 100
PENALTY_SCORE = [-856.75, -60, -20, -856.75, -100]
BASIC_SCORE = 2745900
MAX_SCORE = 14445000


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
    self.sum_penalty: list of int
        ペナルティの累計。
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
        self.sum_penalty = [0] * 5

    def make_next_group(self):
        """
        次のターンの状態を追加する。
        """
        for y in range(self.table):
            for x in range(self.number[y]):
                if self.seats[y][x] != -1:
                    self.seats[y][x] -= 1

    def penalty(self, sit_group):
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
        penalty4_flag: int
            ペナルティ4のフラグ。
        sit_group: list of list
            座れた人の席座標。

        Notes
        -----
        ペナルティ1
            -856.75点
            他の席が空いているのに知らない人が隣りに座ってきた場合。
        ペナルティ2
            -60点
            奇数グループの対面に相手が座った場合。
        ペナルティ3
            -20点
            グループの人数を分けた場合。
        ペナルティ4
            -856.75点
            ペナルティ3において分割しすぎてしまい、孤食が出た場合。
        ペナルティ5
            -100点
            人が座れていなかった場合。
        """
        penalty1_flag = [False, False]
        penalty3_count = 0
        penalty3_flag = 0
        penalty4_flag = 0

        # ペナルティ3, ペナルティ4
        sit_group.sort()
        for bf, af in zip(sit_group, sit_group[1:]):
            if bf[0] == af[0] and bf[1] + 1 == af[1]:
                penalty3_count += 1
            # 隣の席にいなければ分かれているのでペナルティを追加
            else:
                # ペナルティ4の場合
                if penalty3_count == 0:
                    penalty4_flag += 1
                # ペナルティ3の場合
                else:
                    penalty3_flag += 1
                penalty3_count = 0

        self.score[self.index] += penalty3_flag * PENALTY_SCORE[2]
        self.sum_penalty[2] += penalty3_flag

        self.score[self.index] += penalty4_flag * PENALTY_SCORE[3]
        self.sum_penalty[3] += penalty4_flag

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
                    self.sum_penalty[1] += 1

        if all(penalty1_flag):
            self.score[self.index] += PENALTY_SCORE[0]
            self.sum_penalty[0] += 1

        # ペナルティ5
        if self.group_member[0] == self.flag:
            self.group_member.popleft()
            self.group_member.append(random.randint(1, MAX_MEMBER))
        else:
            self.group_member[0] -= self.flag
            self.score[self.index] += self.group_member[0] * PENALTY_SCORE[4]
            self.sum_penalty[4] += self.group_member[0]

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

        # グループ毎の滞在時間
        stay_time = random.randint(MIN_OUT_TIME, MAX_OUT_TIME)

        # 座れた人用の配列
        sit_group = []

        # 指定の席に座らせる
        for place in group:
            if self.seats[place[0]][place[1]] == -1:
                sit_group.append(place)
                self.seats[place[0]][place[1]] = stay_time
                self.score[self.index] += SIT_SCORE
                self.flag += 1

        self.penalty(sit_group)
        self.make_next_group()
        self.score[self.index] += self.score[self.index - 1]

    def show(self):
        directory_path = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_simulation"
        labels = ['penalty1', 'penalty2', 'penalty3', 'penalty4', 'penalty5']
        penalty_score = list(map(lambda x, y: (-x) * y, PENALTY_SCORE, self.sum_penalty))
        # グラフを保存するディレクトリの作成
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
        # 得点の表示
        print(f'総合得点: {sum(self.score)}, 改善率: {((sum(self.score) - BASIC_SCORE) / BASIC_SCORE):.2%}')
        print(f'理論値: {MAX_SCORE} 理論値改善率 {((MAX_SCORE - BASIC_SCORE) / BASIC_SCORE):.2%}')
        # グラフの作成
        make_plot_graph(range(self.index + 1), self.score, "time", "score", "Total score", directory_path, grid=True)
        make_plot_graph(labels, self.sum_penalty, "penalty", "count", "Total penalty", directory_path, bar=True)
        make_plot_graph(labels, penalty_score, "", "", "Percentage of points deducted", directory_path, pie=True)


def make_plot_graph(x, y, x_label, y_label, title, path, bar=False, grid=False, pie=False):
    fig = plt.figure(facecolor='skyblue')
    # 棒グラフの表示
    if bar:
        ax = fig.add_subplot(111, xlabel=x_label, ylabel=y_label, title=title)
        rects = ax.bar(x, y)
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    # スコア推移の表示
    if grid:
        fig.subplots_adjust(left=0.2)
        ax = fig.add_subplot(111, xlabel=x_label, ylabel=y_label, title=title)
        ax.plot(x, y)
        ax.grid(True)
    # ペナルティ割合の表示
    if pie:
        ax = fig.add_subplot(111, title=title)
        ax.pie(y, autopct="%1.1f%%")
        ax.legend(x, fontsize=12, bbox_to_anchor=(0.9, 1))

    fig.savefig(f"{path}/{title}.png", facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())
