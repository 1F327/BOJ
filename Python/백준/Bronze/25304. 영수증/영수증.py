def calculate_receipt(receipt_total, num_items):
    calculated_total = 0
    for _ in range(num_items):
        a, b = map(int, input().split())
        calculated_total += a * b

    if calculated_total == receipt_total:
        print("Yes")
    else:
        print("No")

X = int(input())
N = int(input())
calculate_receipt(X, N)