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