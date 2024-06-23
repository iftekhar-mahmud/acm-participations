def min_total_distance(t, test_cases):
    results = []
    for i in range(t):
        x1, x2, x3 = test_cases[i]
        points = sorted([x1, x2, x3])
        median = points[1]
        total_distance = abs(points[0] - median) + abs(points[1] - median) + abs(points[2] - median)
        results.append(total_distance)
    return results


t = int(input())


test_cases = []
for _ in range(t):
    x1, x2, x3 = map(int, input().split())
    test_cases.append((x1, x2, x3))


results = min_total_distance(t, test_cases)


for result in results:
    print(result)
