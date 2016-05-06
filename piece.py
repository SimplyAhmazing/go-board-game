class Piece(object):
    color = None
    position = None
    board = None

    def __init__(self, color, position, board):
        self.color = color
        self.position = position
        self.board = board

    def get_neighbors(self):
        """
        :return: List of position tuples
        """
        r, c = self.position
        return [
            (r - 1, c),
            (r + 1, c),
            (r, c + 1),
            (r, c - 1),
        ]

    def is_ally(self, piece):
        return not self.is_enemy(piece)

    def is_dead(self, visited=None):
        """
        Determines if a piece is dead using the following logic:

        1. Piece is completely surrounded by enemies -- considered dead
        2. Piece is completely surrounded by enemies & friends -- considered
           alive if friendly neighbors are alive.
        3. Piece is alive if it is not completely surrounded

        :param visited: set with (r, c) position tuples
        :return:
        """

        max_enemy_neighbors_count = 4
        actual_enemy_neighbors_count = 0

        if visited is None:
            visited = set()

        visited.add(self.position)

        for r, c in self.get_neighbors():

            # If we have visited this location then skip it and
            # acknowledge it should not be considered for being an enemy
            if (r, c) in visited:
                max_enemy_neighbors_count -= 1
                continue
            else:
                # Mark current Node as visited
                visited.add((r, c))

            # Retrieve piece at location
            # throws KeyError if r, y coords exceed board size
            try:
                piece = self.board[r][c]
            except KeyError:
                max_enemy_neighbors_count -= 1
                continue

            # If a piece's neighbor doesn't exist, it is alive
            if piece is None:
                return False

            # Acknowledge enemy neighbor
            if piece.is_enemy(self):
                actual_enemy_neighbors_count += 1
                continue

            # If neighbor is an ally, determine if the neighbor is dead
            if piece.is_ally(self):
                is_alive = not piece.is_dead(visited)

                if is_alive:
                    return False
                else:
                    max_enemy_neighbors_count -= 1

        return (max_enemy_neighbors_count == actual_enemy_neighbors_count)

    def is_enemy(self, piece):
        return (self.color != piece.color)

    def __str__(self):
        return self.color.name.upper()[0]
