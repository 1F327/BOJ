def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("1\n")
    else:
        print("0\n")

input_year = int(input())
is_leap_year(input_year)