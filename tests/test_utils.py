import unittest

from colors import Color
from exceptions import IllegalGoPieceColorException
from utils import create_board_from_str, piece_str_to_color


class CreateBoardFromStrTestCase(unittest.TestCase):
    def test_create_board_from_str(self):
        board_str = """
        www
        wbw
        ww-
        """

        board = create_board_from_str(board_str)

        # Verify board dimensions
        self.assertEqual(3, board.size)
        self.assertEqual(3, len(board.grid))
        self.assertEqual(3, len(board.grid[0]))

        # Verify piece arrangements
        self.assertEqual(board[0][0].color, Color.white)
        self.assertEqual(board[0][1].color, Color.white)
        self.assertEqual(board[0][2].color, Color.white)
        self.assertEqual(board[1][0].color, Color.white)
        self.assertEqual(board[1][1].color, Color.black)
        self.assertEqual(board[1][2].color, Color.white)
        self.assertEqual(board[2][0].color, Color.white)
        self.assertEqual(board[2][1].color, Color.white)
        self.assertIsNone(board[2][2])


class PieceStrToColorTestCase(unittest.TestCase):
    def test_piece_str_to_color(self):
        with self.assertRaises(IllegalGoPieceColorException) as e:
            piece_str_to_color('r')

        self.assertEqual(piece_str_to_color('w'), Color.white)
        self.assertEqual(piece_str_to_color('b'), Color.black)
        self.assertEqual(piece_str_to_color('W'), Color.white)
        self.assertEqual(piece_str_to_color('B'), Color.black)



if __name__ == '__main__':
    unittest.main()
