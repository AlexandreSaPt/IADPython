string = input("") #string

string = string.split(" ") # list

for idx in range(len(string)):
    print(string[len(string) - idx - 1], end="")
    if idx + 1 == len(string):
        print()
    else:
        print(" ", end="")

