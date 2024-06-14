def optimal(n):
    max_sum = 0
    optimal = 0
    for x in range(2, n+1):
        k = n // x
        current_sum = x * k * (k + 1) // 2
        if current_sum > max_sum:
            max_sum = current_sum
            optimal = x
    return optimal


user_input = int(input())
for _ in range (user_input):
    n = int(input())
    result = optimal(n)
    print(result)