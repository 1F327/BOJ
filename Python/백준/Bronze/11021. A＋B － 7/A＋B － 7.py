def sum_2_numbers(case):
    for i in range(case):
        A, B = map(int, input().split())
        print(f"Case #{i + 1}: {A + B}")
            
T = int(input())
sum_2_numbers(T)