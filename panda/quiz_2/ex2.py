import numpy as np

init_matrix = list()


line = input()
line = line.split(",")
init_matrix.append(line)
count = len(line)
for i in range(count - 1):
    line = input()
    line = line.split(",")
    init_matrix.append(line)

a = np.array(init_matrix, dtype=np.float64)    

line = input()
line = line.split(",")

b = np.array(line, dtype=np.float64)

sol = np.linalg.solve(a, b)

print("solution:")
print(sol)