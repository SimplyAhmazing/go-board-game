import unittest

from utils import create_board_from_str
from colors import Color
from piece import Piece


class PieceTestCase(unittest.TestCase):
    def setUp(self):
        self.white_piece = Piece(Color.white, (0,0), None)
        self.black_piece = Piece(Color.black, (0,0), None)

    def test_piece_as_str(self):
        self.assertEqual("B", str(self.black_piece))
        self.assertEqual("W", str(self.white_piece))

    def test_piece_get_neighbors(self):
        expected = sorted([(-1, 0), (1, 0), (0, -1), (0, 1)])
        result = sorted(self.white_piece.get_neighbors())
        self.assertListEqual(expected, result)

    def test_is_ally(self):
        self.assertFalse(self.white_piece.is_ally(self.black_piece))

    def test_is_enemy(self):
        self.assertTrue(self.white_piece.is_enemy(self.black_piece))


class PieceIsDeadAlgorithmTestCase(unittest.TestCase):
    def test_one_piece_on_board(self):
        board_str = """
        - - - - -
        - - - - -
        - - W - -
        - - - - -
        - - - - -
        """

        board = create_board_from_str(board_str)
        p = board[2][2]
        self.assertFalse(p.is_dead())

    def test_one_piece_surrounded(self):
        board = """
        - - - - -
        - - B - -
        - B W B -
        - - B - -
        - - - - -
        """

        board = create_board_from_str(board)
        p = board[2][2]
        self.assertTrue(p.is_dead())

    def test_two_pieces_partially_surrouned(self):
        board = """
        - - - - -
        - - B - -
        - B W W B
        - - B B -
        - - - - -
        """

        board = create_board_from_str(board)
        p = board[2][2]
        self.assertFalse(p.is_dead())

    def test_two_pieces_completely_surrouned(self):
        board = """
        - - - - -
        - - B B -
        - B W W B
        - - B B -
        - - - - -
        """

        board = create_board_from_str(board)
        p = board[2][2]
        self.assertTrue(p.is_dead())


    def test_multiple_pieces_completely_surrouned(self):
        board = """
        - - - B - -
        - - B W B -
        - B W W B -
        - B W W B -
        - - B W B -
        - - - B - -
        """

        board = create_board_from_str(board)
        p = board[2][2]
        self.assertTrue(p.is_dead())


if __name__ == '__main__':
    unittest.main()
