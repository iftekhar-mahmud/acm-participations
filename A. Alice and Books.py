
def max_pages_read(t, test_cases):
    results = []
    for i in range(t):
        n, books = test_cases[i]

        # Find the maximum and minimum elements in the list
        max1 = max2 = -1
        min1 = min2 = float('inf')

        for pages in books:
            if pages > max1:
                max2 = max1
                max1 = pages
            elif pages > max2:
                max2 = pages

            if pages < min1:
                min2 = min1
                min1 = pages
            elif pages < min2:
                min2 = pages

        # Calculate max read pages based on the number of books
        if n > 3:
            max_read = max1 + min1
        else:
            max_read = max1 + max2

        results.append(max_read)

    return results


t = int(input())


test_cases = []


for _ in range(t):
    n = int(input())
    books = list(map(int, input().split()))
    test_cases.append((n, books))


results = max_pages_read(t, test_cases)


for result in results:
    print(result)
