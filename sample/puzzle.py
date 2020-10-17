from cafe import Cafeteria, TOYOTA


def sit_check(number, count, flag=-1):
    global env
    res = []
    for i, table in enumerate(env.seats):
        # 連続で空いているテーブル数のカウント
        max_table_count = 0
        max_index = 0
        table_count = 0
        index = 0
        for j, seat in enumerate(table):
            if seat == -1:
                # indexをメモしておく
                if table_count == 0:
                    index = j
                table_count += 1
            else:
                # 空いている数が最大のとき
                if max_table_count < table_count:
                    max_table_count = table_count
                    max_index = index
                # 初期化
                table_count = 0
                index = 0
        if max_table_count < table_count:
            max_table_count = table_count
            max_index = index

        # 座れるかのチェック
        if max_table_count == number and i > flag:
            for j, seat in enumerate(table):
                # 空席の場合
                if seat == -1 and max_index <= j:
                    count -= 1
                    res.append([i, j])
                    # 全員座った時
                    if count == 0:
                        break
            return res, i

    return False, False


def all_sit_check(member):
    if member != 7:
        res, i = sit_check(6, member)
        if res:
            return res, i
    else:
        res1, i = sit_check(6, 3)
        if res1:
            res2, _ = sit_check(6, 4, i)
            if res2:
                return res1 + res2, i
            return res1, False

    return False, False


def member_check(order, number, flag=-1):
    for i in order:
        res, i = sit_check(i, number, flag)
        if res:
            return res, i

    return False, False


def double_check(number1, number2):
    res1, i = member_check(order[number1], number1)
    if res1:
        res2, j = member_check(order[number2], number2, flag=i)
        if res2:
            return res1 + res2, j
    return False, False


def triple_check(number1, number2, number3):
    res12, j = double_check(number1, number2)
    if res12:
        res3, _ = member_check(order[number3], number3, j)
        if res3:
            return res12 + res3
    return res12


def get_action(member):
    global env
    # 席が全て空いているとき
    res, flag = all_sit_check(member)
    if res and flag > -1:
        return res
    # 片方だけ全て席が空いている
    elif res:
        member = 4
    res, _ = sit_check(member, member)
    if res:
        return res

    # 1 -> 3 -> 2 -> 4 -> 待機
    if member == 1:
        res, _ = member_check(order[member], member)
