from cafe import Cafeteria, TOYOTA


TIME = 100


def greedy(next_member, y, x, table, number):
    res = []
    for _ in range(next_member):
        if number == x:
            x = 0
            y += 1
        if table == y:
            y = 0
        res.append([y, x])
        x += 1

    return res, y, x


y, x = 0, 0
env = Cafeteria(TOYOTA.data, TIME)
for _ in range(TIME):
    process, y, x = greedy(env.group_member[0], y, x, TOYOTA.TABLE, TOYOTA.NUMBER)
    env.run(process)
env.show()
