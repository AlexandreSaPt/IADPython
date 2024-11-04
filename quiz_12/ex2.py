'''
    Given a square matrix A (dimension N x N) write a program that exchanges the minimum value element with the maximum value element.
    input order (one per line): N, A[0][...], A[1][...], ...
'''

def printMatriz(rows, columns, matriz):
    for r in range(rows):
        print("[", end="")
        for c in range(columns):
            print(f"{matriz[r][c]}", end="")
            if c + 1 != columns:
                print(", ", end="")
        print("]")
    

maxValue = 0
maxIsSet = False

rowMax = 0
columnMax = 0

minValue = 0
minIsSet = False

rowMin = 0
columnMin = 0


N = int(input("")) #rows and columns

matrizA = [[0] * (N) for i in range(N)] # inicialização de uma matriz NxM com tudo zeros

for row in range(N):
    for column in range(N):
        matrizA[row][column] = float(input(""))
        if minIsSet == False or matrizA[row][column] < minValue:
            minIsSet = True
            minValue = matrizA[row][column]
            rowMin = row
            columnMin = column
            continue
        
        if maxIsSet == False or matrizA[row][column] > maxValue:
            maxIsSet = True
            maxValue = matrizA[row][column]
            rowMax = row
            columnMax = column

matrizA[rowMax][columnMax] = minValue

matrizA[rowMin][columnMin] = maxValue

printMatriz(N, N, matrizA)