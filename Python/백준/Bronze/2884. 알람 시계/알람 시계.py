def calculate_alarm_time(h, m):
    m -= 45
    if m < 0:
        m += 60
        h -= 1
        if h < 0:
            h += 24
    return h, m

H, M = map(int, input().split())
H, M = calculate_alarm_time(H, M)
print(H, M)
