from board import Board
from colors import Color
from exceptions import IllegalGoPieceColorException


def piece_str_to_color(color_str):
    """
    Maps single letters to piece Color enum

    :param color_str: str
    :return: Color enum
    """

    color_str = color_str.lower()

    COLORS_MAP = {
        'w': Color.white,
        'b': Color.black
    }

    if color_str not in COLORS_MAP:
        raise IllegalGoPieceColorException(
            "Invalid color string: {}".format(color_str)
        )

    return COLORS_MAP[color_str]


def create_board_from_str(board_str, empty_location_str='-'):
    """
    :param board_str: str representing desired board configuration
    :return: Board
    """

    # Remove spaces
    board_str = board_str.replace(' ', '')

    # Split by lines
    board_rows = board_str.split('\n')

    # Remove empty lines
    board_rows = [row for row in board_rows if row]

    board = Board(len(board_rows))

    for r, row in enumerate(board_rows):
        for c, piece_color_str in enumerate(row):
            if piece_color_str == empty_location_str: continue

            color = piece_str_to_color(piece_color_str)
            board.add(color=color, position=(r,c))

    return board
