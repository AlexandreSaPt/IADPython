'''
1   2   9
5   4   3
3   8   1
'''

#get input 
#given a matrix NxN with the following order "N, A[0][...], A[1][...], ..."


def printMatrix(rows, columns, matriz):
    for r in range(rows):
        print("[", end="")
        for c in range(columns):
            print(f"{matriz[r][c]}", end="")
            if c + 1 != columns:
                print(", ", end="")
        print("]")

'''
def getInput(N, matrix):
    for c in range(N):
        for r in range(N):
            matrix[r][c] = float(input(""))
            print(f"matrix[{r}][{c}] = {matrix[r][c]}")
'''



N = int(input(""))
matrix = [[0] * (N) for i in range(N)] # inicialização de uma matriz NxM com tudo zeros

maxColumn = 0
hasMaxColumn = False

orderRows = 0



for r in range(N):
        for c in range(N):
            matrix[r][c] = float(input(""))



for c in range(N):
        maxColumn = 0
        hasMaxColumn = False
        for r in range(c, N):
            if ( abs(matrix[r][c]) > maxColumn or hasMaxColumn == False) and (r >= c):
                hasMaxColumn = True
                maxColumn = abs(matrix[r][c])
                orderRows = r
        matrix[c], matrix[orderRows] = matrix[orderRows], matrix[c]



  



printMatrix(N, N, matrix)        