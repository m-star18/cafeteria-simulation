from cafe import Cafeteria, TOYOTA


TIME = 300


def new_greedy(member):
    global env
    res = []
    for i, table in enumerate(env.seats):
        for j, seat in enumerate(table):
            if seat == -1:
                member -= 1
                res.append([i, j])
            if member == 0:
                return res
    return res


y, x = 0, 0
env = Cafeteria(TOYOTA.data, TIME)
for _ in range(TIME):
    process = new_greedy(env.group_member[0])
    env.run(process)
env.show()
