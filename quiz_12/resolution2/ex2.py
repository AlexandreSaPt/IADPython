def printMatrix(rows, columns, matriz):
    for r in range(rows):
        print("[", end="")
        for c in range(columns):
            print(f"{matriz[r][c]}", end="")
            if c + 1 != columns:
                print(", ", end="")
        print("]")

N = int(input(""))

numbers = [0]*(N * N)

for idx in range(N * N):
    numbers[idx] = float(input(""))

numbers.sort()

answerList = [[0] * (N) for i in range(N)] # inicialização de uma matriz NxM com tudo zeros

for r in range(N):
    for c in range(N):
        answerList[r][c] = numbers[N*r + c]

printMatrix(N, N, answerList)
