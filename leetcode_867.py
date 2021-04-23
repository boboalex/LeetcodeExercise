if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6]]
    m, n = len(matrix), len(matrix[0])
    res = [[0] * m for _ in range(n)]
    print(res)
