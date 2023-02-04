matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]


def rotate(matrix) -> None:
    matrix[:] = zip(*matrix[::-1])


rotate(matrix)
print(matrix)
