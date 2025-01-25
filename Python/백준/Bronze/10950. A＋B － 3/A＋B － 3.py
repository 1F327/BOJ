def add_two_numbers(case):
    for _ in range(case):
        A, B = map(int, input().split())
        print(A + B)

T = int(input())
add_two_numbers(T)
