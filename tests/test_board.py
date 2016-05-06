import unittest

from colors import Color
from exceptions import IllegalMoveException
from utils import create_board_from_str


class BoardTestCase(unittest.TestCase):
    def setUp(self):
        board_str = """
            WWW
            WBW
            WW-
        """

        self.board = create_board_from_str(board_str)

    def test_board_as_str(self):
        self.assertEqual("WWW\nWBW\nWW-", str(self.board))

    def test_illegal_add_move(self):
        with self.assertRaises(IllegalMoveException) as e:
            self.board.add(Color.black, (0, 0))

    def test_legal_add_move(self):
        self.board.add(Color.white, (2, 2))
        self.assertEqual(self.board[2][2].color, Color.white)

    def test__getitem__(self):
        expected = self.board.grid[2][2]
        result = self.board[2][2]
        self.assertEqual(expected, result)
