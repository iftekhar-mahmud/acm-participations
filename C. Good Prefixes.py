# Doesn't Work
def good_prefix(n, arr):
    prefix_sum = 0
    good_prefix_count = 0

    for i in range(n):
        prefix_sum += arr[i]
        if arr[i] == prefix_sum:
            good_prefix_count += 1

    return good_prefix_count

user_input = int(input())
result = []
for _ in range(user_input):
    n = int(input())
    arr = list(map(int, input().split()))
    result.append(good_prefix(n, arr))

for res in result:
    print(res)
