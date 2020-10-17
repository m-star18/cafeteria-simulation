from cafe import Cafeteria, TOYOTA
from random import randint


TIME = 300
env = Cafeteria(TOYOTA.data, TIME)
for _ in range(TIME):
    process = [[randint(0, 49), randint(0, 5)] for _ in range(env.group_member[0])]
    env.run(process)
env.show()
