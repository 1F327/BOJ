def add_two_numbers(T):
    for _ in range(T):
        A, B = map(int, input().split())
        print(A + B)

T = int(input())
add_two_numbers(T)