import numpy as np

print("Number of rows =", end="")
n_rows = int(input())

print("Number of columns =", end="")
n_col = int(input())

init_matrix = list()

for r in range(n_rows):
    helper = list()
    for c in range(n_col):
        print(f"a[{r}][{c}]=", end="")
        n = float(input())
        helper.append(n)
    
    init_matrix.append(helper)


print("Matrix transpose:")

matrix = np.array(init_matrix, dtype=np.float64)

transpose = (matrix.transpose())

transpose = str(transpose)

transpose = transpose[1:-1]

print(transpose)
