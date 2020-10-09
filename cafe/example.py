class Toyota:
    def __init__(self):
        self.TABLE = 50
        self.NUMBER = 6
        self.SUM_NUMBER = [self.NUMBER] * self.TABLE
        self.SEATS = [[-1] * self.NUMBER for _ in range(self.TABLE)]
        self.data = [self.TABLE, self.SUM_NUMBER, self.SEATS]


def basic_algorithm(next_member, seats, number):
    # ７人は一人余ってしまうので別れる
    if next_member == 7:
        group_member = [4, 3]
    else:
        group_member = [next_member]

    # 配列用
    number -= 1

    res = []
    pop_index = []
    for i, member in enumerate(group_member):
        for y, seat in enumerate(seats):
            if all(table == -1 for table in seat):
                res += [[y, x] for x in range(member)]
                pop_index.append(i)
                break

    group_member = [i for i in range(len(group_member)) if i not in pop_index]

    # 全員で座れない場合、一人になってしまう場合は待機
    while group_member and 1 not in group_member:
        flag = False
        pop_index = []
        for i, member in enumerate(group_member):
            for y, seat in enumerate(seats):
                # 全員着席可能の場合
                if member <= seat.count(-1):
                    for x, table in enumerate(seat):
                        if table == -1 and member > 0:
                            member -= 1
                            res.append([y, x])
                    pop_index.append(i)
                    flag = True
                    break
            if flag:
                break
        # 座れなかった場合、グループを半分にして試す
        else:
            group_member.append(group_member[0] // 2)
            group_member[0] -= group_member[-1]

        group_member = [i for i in range(len(group_member)) if i not in pop_index]

    return res
