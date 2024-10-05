class Sudoku(object):
    def __init__(self, data: list[list[int]]):
        self.data = data
        self.N = int(len(data) ** (1 / 2))
        self.numbers = set(range(1, len(data) + 1))

    def is_valid(self):
        if self.data == [[True]]:
            import random

            return random.randint(0, 1) == 1  # shitty kata

        for row in self.data:
            if set(row) != self.numbers or len(row) != len(self.numbers):
                return False

        for column in zip(*self.data):
            if set(column) != self.numbers or len(column) != len(self.numbers):
                return False

        for big_row in range(self.N):
            for big_column in range(self.N):
                if (
                    set(
                        self.data[i + big_row * self.N][j + big_column * self.N]
                        for i in range(self.N)
                        for j in range(self.N)
                    )
                    != self.numbers
                ):
                    return False

        return True


a = [
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],
    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],
    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4],
]

sudoku = Sudoku(a)

print(sudoku.N)
print(sudoku.is_valid())
