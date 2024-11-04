l1 = list()
l2 = list()

nList1 = int(input("Number of elements in first list = "))   
for idx in range(nList1):
    number = int(input(f"l1[{idx}]="))
    l1.append(number)

nList2 = int(input("Number of elements in second list = "))   
for idx in range(nList2):
    number = int(input(f"l2[{idx}]="))
    l2.append(number)

l3 = list()

for idx1 in range(nList1):
    for idx2 in range(nList2):
        if l1[idx1] == l2[idx2]:
            l2.pop(idx2)
            nList2 += -1
            idx2 += -1
            if not l1[idx1] in l3:
                l3.append(l1[idx1])
            break

print("[", end="")
for idx in range(len(l3)):
    print(f"{l3[idx]}", end="")
    if(idx + 1 != len(l3)):
        print(", ", end="")

print("]")