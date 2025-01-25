def calculate_prize(d1, d2, d3):
    if d1 == d2 == d3:
        print(10000 + d1 * 1000)
    elif d1 == d2 or d1 == d3:
        print(1000 + d1 * 100)
    elif d2 == d3:
        print(1000 + d2 * 100)
    else:
        print(max(d1, d2, d3) * 100)

dice1, dice2, dice3 = map(int, input().split())
calculate_prize(dice1, dice2, dice3)
