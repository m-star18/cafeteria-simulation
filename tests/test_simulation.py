import unittest

from cafe import Cafeteria


class TestCombination(unittest.TestCase):
    def setUp(self):
        TABLE = 30
        NUMBER = [6] * TABLE
        SEATS = [[-1] * 6 for _ in range(TABLE)]
        self.TIME = 20
        self.cafeteria_data = [TABLE, NUMBER, SEATS]

    def tearDown(self):
        pass

    def test_close(self):
        env = Cafeteria(self.cafeteria_data, self.TIME)
        for _ in range(self.TIME):
            env.run([])
        self.assertEqual(list(range(0, -((self.TIME + 1) * 300), -300)), env.score)


if __name__ == '__main__':
    unittest.main()
