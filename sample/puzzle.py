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
