import unittest
import frog_jump_seconds


class TestFrogJumpSeconds(unittest.TestCase):
    def test_can_jump(self):
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        X = 5
        result = frog_jump_seconds.solution(X, A)
        self.assertEqual(result, 6)

    def test_cant_jump(self):
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        X = 7
        result = frog_jump_seconds.solution(X, A)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
