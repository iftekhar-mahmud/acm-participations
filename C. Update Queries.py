def update_string(s, ind, c):
    s = list(s)
    for i in range(len(ind)):
        s[ind[i] - 1] = c[i]
    return ''.join(s)


def find_smallest_lexicographic(s):
    return ''.join(sorted(s))


def solve():
    t = int(input())  # Number of test cases

    for _ in range(t):
        n, m = map(int, input().split())  # Length of string and number of updates
        s = input().strip()  # Original string
        ind = list(map(int, input().split()))  # Array of indices
        c = input().strip()  # Update string

        updated = update_string(s, ind, c)
        result = find_smallest_lexicographic(updated)
        print(result)


if __name__ == "__main__":
    solve()