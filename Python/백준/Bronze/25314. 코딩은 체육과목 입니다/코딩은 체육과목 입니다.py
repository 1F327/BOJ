def print_data_type(byte_size):
    for _ in range(byte_size // 4):
        print("long", end=" ")
    print("int")

N = int(input())
print_data_type(N)