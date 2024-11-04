fileName1 = input("Filename 1:")
fileName2 = input("Filename 2:")

f1Read = open(fileName1, 'r')
f2Read = open(fileName2, 'r')


values1 = list()
for line in f1Read:
    line.strip()
    values1.append(float(line))


values2 = list()
for line in f2Read:
    line.strip()
    values2.append(float(line))

maxLength = 0
len_val1 = len(values1)
len_val2 = len(values2)

if len_val2 > len_val1:
    maxLength = len(values2)
else:
    maxLength = len(values1)


for idx in range(maxLength):
    n1 = 0
    if idx >= len_val1:
        n1 = 0
    else:
        n1 = values1[idx]

    n2 = 0
    if idx >= len_val2:
        n2 = 0
    else:
        n2 = values2[idx]


    print(f"{(n1 + n2) / 2}")

