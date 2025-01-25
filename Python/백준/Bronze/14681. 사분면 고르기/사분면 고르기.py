def get_quadrant(a, b):
    if a > 0 and b > 0:
        print("1")
    elif a < 0 < b:
        print("2")
    elif a < 0 and b < 0:
        print("3")
    else:
        print("4")

x = int(input())
y = int(input())
get_quadrant(x, y)
