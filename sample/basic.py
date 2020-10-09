from cafe import Cafeteria, TOYOTA, basic


TIME = 300

env = Cafeteria(TOYOTA.data, TIME)
for _ in range(TIME):
    process = basic(env.group_member[0], env.seats, TOYOTA.NUMBER)
    env.run(process)
env.show()
