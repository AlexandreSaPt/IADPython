'''
Given as input the csv filename, the column name and the name of a function (max, min, sum), calculate the value of the given function for the values of the given column. For example, given the following file: "ginasio.csv" and the column name: "altura" and the function: "max", the answer should be: 166

'''

#get name of file
nameOfFile = input("Filename:")
columnName = input("Column name:")
functionName = input("Function name:")


#get data from text file
fRead = open(nameOfFile, 'r')

headers = fRead.readline().strip()

headers = headers.split(";")

idxColumn = 0
idx = 0
for h in headers:
    if h == columnName:
        idxColumn = idx
        break
    idx += 1

#get a list of only the column we want
elements = list()

for line in fRead:
    line = line.strip()

    listValues = line.split(";")

    value = 0
    if listValues[idxColumn].isnumeric():
        value = float(listValues[idxColumn])
    else:
        value = listValues[idxColumn]

    elements.append(value)


answer = 0.0

if(functionName == "max"):
    answer = max(elements)
elif functionName == "min":
    answer = min(elements)
elif functionName == "sum":
    answer = sum(elements)


print(f"{functionName}({columnName})={float(answer):.2f}")