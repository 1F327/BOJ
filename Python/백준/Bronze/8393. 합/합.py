def sum_1_to_N(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    print(total_sum)

N = int(input())
sum_1_to_N(N)