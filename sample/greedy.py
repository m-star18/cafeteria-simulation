from cafeteria import Cafeteria


TIME = 20
TABLE = 30
NUMBER = [6] * TABLE
SEATS = [[-1] * 6 for _ in range(TABLE)]


def greedy(next_member, y, x, flag):
    res = []
    for _ in range(next_member):
        if flag == x:
            x = 0
            y += 1
        res.append([y, x])
        x += 1

    return res, y, x


cafeteria_data = [TABLE, NUMBER, SEATS]
y, x = 0, 0
env = Cafeteria(cafeteria_data, TIME)
for _ in range(TIME):
    process, y, x = greedy(env.group_member[0], y, x, 6)
    env.run(process)
env.show()
