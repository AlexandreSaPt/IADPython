#Given an integer value determine its factors (numbers that divide the given number) using the for loop.

inputValue = int(input("Factors of:"))

for i in range(1, inputValue + 1):
    if inputValue % i == 0:
        print(i)