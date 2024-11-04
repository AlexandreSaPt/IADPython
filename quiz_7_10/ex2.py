intList = list()

nList1 = int(input("Number of elements in the list = "))   
for idx in range(nList1):
    number = int(input(f"l1[{idx}]="))
    intList.append(number)

nGreatestEl = int(input("Number of greatest elements = "))

intList.sort(reverse = True)

print("[", end="")

for idx in range(nGreatestEl):
    print(f"{intList[idx]}", end="")
    if(idx + 1 != (nGreatestEl)):
        print(", ", end="")

print("]")