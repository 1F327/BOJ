def add_minutes_to_time(H, M, min_to_add):
    H += min_to_add // 60
    extra_hour, M = divmod(M + (min_to_add % 60), 60)
    H += extra_hour
    H %= 24
    return H, M

A, B = map(int, input().split())
C = int(input())
A, B = add_minutes_to_time(A, B, C)
print(A, B)
