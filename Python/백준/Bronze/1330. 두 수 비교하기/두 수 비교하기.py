def compare_numbers(n1, n2):
    if n1 > n2:
        print(">")
    elif n1 < n2:
        print("<")
    else:
        print("==")

A, B = map(int, input().split())
compare_numbers(A, B)
