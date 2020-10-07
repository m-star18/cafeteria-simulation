import unittest

from cafe import Cafeteria, TOYOTA


class TestCombination(unittest.TestCase):
    def setUp(self):
        self.TIME = 100

    def tearDown(self):
        pass

    def test_close(self):
        env = Cafeteria(TOYOTA.data, self.TIME)
        for _ in range(self.TIME):
            env.run([])
        self.assertEqual(list(range(0, -((self.TIME + 1) * 600), -600)), env.score)


if __name__ == '__main__':
    unittest.main()
