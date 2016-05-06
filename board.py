from exceptions import IllegalMoveException
from piece import Piece


class Board(object):
    """
    Represents a Go board which can add (place) pieces.
    """

    def __init__(self, size : int):
        self.size = size

        # All Go boards are square sized
        self.grid = [[None]*size for _ in range(size)]

    def add(self, color, position):
        self.validate_position(position)
        p = Piece(color, position, self)
        r, c = position
        self.grid[r][c] = p

    def validate_position(self, position : (int, int)):
        r, c = position

        # Piece (r,c) Coords must be within board size
        if not (0 <= r < self.size) or not (0 <= c < self.size):
            raise IllegalMoveException(
                'Piece position: {} out of {}x{} board size'
                .format(position, self.size, self.size)
            )

        if self.grid[r][c] is not None:
            raise IllegalMoveException(
                "Board position ({}, {}) has an existing piece."
                .format(r, c)
            )


    def __str__(self):
        """
        Prints Piece string in a row by row fashion, prints '-' where a piece
        is missing.

        :return:
        """
        return '\n'.join([
            ''.join([
                (str(p) if p else '-')
                for p in row
            ])
            for row in self.grid
        ])

    def __getitem__(self, item):
        return self.grid[item]
