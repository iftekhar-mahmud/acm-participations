user_input = int(input())
for i in range (user_input):
    a, b = input().split()


    new_a = b[0] + a[1:]
    new_b = a[0] + b[1:]

    print(new_a, new_b)
