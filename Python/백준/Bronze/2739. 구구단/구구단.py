def print_multiplication_table(number):
    for i in range(1, 10):
        result = number * i
        print(f"{number} * {i} = {result}")
        
N = int(input())
print_multiplication_table(N)