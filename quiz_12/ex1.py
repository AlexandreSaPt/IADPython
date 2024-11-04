'''
    Given a matrix A (dimension N x M) write a program that adds a new column and a new row to the given matrix, containing, respectively, the sum of each row and the sum of each column.
    input order (one per line): N, M, A[0][...], A[1][...], ...
'''

#Matriz A (NxM)


def printMatriz(rows, columns, matriz):
    for r in range(rows):
        print("[", end="")
        for c in range(columns):
            print(f"{matriz[r][c]}", end="")
            if c + 1 != columns:
                print(", ", end="")
        print("]")




N = int(input("")) #rows
M = int(input("")) #columns

matrizA = [[0] * (M + 1) for i in range(N + 1)] # inicialização de uma matriz NxM com tudo zeros

for row in range(N):
    rowSum = 0
    for column in range(M):
        matrizA[row][column] = float(input(""))
        print(f"matriz[{row}][{column}] = {matrizA[row][column]}")
        rowSum += matrizA[row][column]
    matrizA[row][M] = rowSum

for column in range(M + 1):
    columnSum = 0
    for row in range(N + 1):
        columnSum += matrizA[row][column]

    matrizA[N][column] = columnSum

printMatriz(N+1, M+1, matrizA)




