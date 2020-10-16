from cafe import Cafeteria, TOYOTA


TIME = 300


def greedy(next_member, table, number):
    global y, x
    res = []
    for _ in range(next_member):
        if number == x:
            x = 0
            y += 1
        if table == y:
            y = 0
        res.append([y, x])
        x += 1

    return res


y, x = 0, 0
env = Cafeteria(TOYOTA.data, TIME)
for _ in range(TIME):
    process = greedy(env.group_member[0], TOYOTA.TABLE, TOYOTA.NUMBER)
    env.run(process)
env.show()
