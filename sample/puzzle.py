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
