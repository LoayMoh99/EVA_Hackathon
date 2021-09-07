# Loay Mohamed
# Challeng 6:

matrix = input("Input your binary n*m matrix:")
#matrix = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
# matrix = [[1, 0], [0, 1]]
n = len(matrix)
m = len(matrix[0])
# check and validate matrix dimensions:
if m == 0 or n == 0:
    print("Invalid Matrix with dimensions " + str(n) + " , " + str(m))
for i in range(n):
    if len(matrix[i]) != m:
        print("Invalid Matrix with dimensions " + str(n) + " , " + str(m))


def swapRows(row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]


def swapCols(col1, col2):
    matrix[:, [col1, col2]] = matrix[:, [col2, col1]]


def checkMatrix():
    # if any row in the matrix not equal to the first row or reverse of it..
    for i in range(0, n):
        for j in range(0, n):
            if(matrix[0][0] ^ matrix[0][j] ^ matrix[i][0] ^ matrix[i][j] != 0):
                return -1
    rowSum = 0
    colSum = 0
    rowSwap = 0
    colSwap = 0
    for i in range(0, n):
        rowSum = rowSum + matrix[i][0]
        colSum = colSum + matrix[0][i]
        rowSwap += matrix[i][0] == i % 2
        colSwap += matrix[0][i] == i % 2

    # count of 1's in each row must equal count 0's or at most differ by 1 (in case odd number matrix board)
    if(rowSum != n//2 and rowSum != (n + 1)//2):
        return -1
    if(colSum != n//2 and colSum != (n + 1)//2):
        return -1
    if(n % 2 == 1):
        if(colSwap % 2):
            colSwap = n - colSwap
        if(rowSwap % 2):
            rowSwap = n - rowSwap
    else:
        colSwap = min(colSwap, n - colSwap)
        rowSwap = min(rowSwap, n - rowSwap)
    return (rowSwap + colSwap) // 2


print(checkMatrix())
