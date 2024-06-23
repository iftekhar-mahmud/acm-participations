def stabilize_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    changed = True

    while changed:
        changed = False
        new_matrix = [row[:] for row in matrix]

        for i in range(rows):
            for j in range(cols):
                neighbors = []
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbors.append(matrix[ni][nj])

                if neighbors and matrix[i][j] > max(neighbors):
                    new_matrix[i][j] = max(neighbors)
                    changed = True

        matrix = new_matrix

    return matrix


def main():
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        matrix = [list(map(int, input().split())) for _ in range(n)]

        result = stabilize_matrix(matrix)

        for row in result:
            print(*row)

        print()  


if __name__ == "__main__":
    main()