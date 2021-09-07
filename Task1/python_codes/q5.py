# Loay Mohamed
# Challeng 5:

# used to help in generating combinations for 1's and 0's to represent possible student orientations..
from itertools import product
import numpy as np


#matrix = input("Input the seats matrix:")
matrix = [["#", ".", ".", ".", "#"], [".", "#", ".", "#", "."], [
    ".", ".", "#", ".", "."], [".", "#", ".", "#", "."], ["#", ".", ".", ".", "#"]]
# matrix = [[".", "#"], ["#", "#"], [
#     "#", "."], ["#", "#"], [".", "#"]]
# matrix = [["#", ".", "#", "#", ".", "#"], [
#     ".", "#", "#", "#", "#", "."], ["#", ".", "#", "#", ".", "#"]]

n = len(matrix)
m = len(matrix[0])
answer = []
studCount = 0
# check and validate matrix dimensions:
if m == 0 or n == 0:
    print("Invalid Matrix with dimensions " + str(n) + " , " + str(m))
for i in range(n):
    if len(matrix[i]) != m:
        print("Invalid Matrix with dimensions " + str(n) + " , " + str(m))
    answer.append(list())
    # -1 -> broken chair , 0 -> good chair but empty , 1->good chair with student in it..
    for j in range(m):
        if matrix[i][j] == "#":
            answer[i].append(-1)
        if matrix[i][j] == ".":
            answer[i].append(1)
            studCount += 1

studentsCombinations = [i for i in product(
    range(2), repeat=studCount)]
studentsCombinations = np.array(studentsCombinations)


def changeOrientation(indx):
    currOrien = studentsCombinations[indx]
    ind = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == ".":
                answer[i][j] = currOrien[ind]
                ind += 1
                if ind == studCount:
                    return


def checkOrientation():
    for i in range(n):
        for j in range(m):
            if answer[i][j] == 1:  # student is there then check neighbors
                if i < n-1 and j > 0 and j < m-1:
                    if answer[i][j-1] == 1 or answer[i][j+1] == 1 or answer[i+1][j-1] == 1 or answer[i+1][j+1] == 1:
                        return False
                elif i < n-1 and j == 0:
                    if answer[i][j+1] == 1 or answer[i+1][j+1] == 1:
                        return False
                elif i < n-1 and j == m-1:
                    if answer[i][j-1] == 1 or answer[i+1][j-1] == 1:
                        return False
                elif i == n-1 and j > 0 and j < m-1:
                    if answer[i][j-1] == 1 or answer[i][j+1] == 1:
                        return False
                elif i == n-1 and j == 0:
                    if answer[i][j+1] == 1:
                        return False
                elif i == n-1 and j == m-1:
                    if answer[i][j-1] == 1:
                        return False
    return True


finalCount = 0
currentOrienIndex = len(studentsCombinations)-1

for i in range(currentOrienIndex, 0, -1):
    changeOrientation(i)
    if checkOrientation():
        cnt = 0
        for ii in range(studCount):
            if studentsCombinations[i][ii] == 1:
                cnt += 1
            finalCount = max(finalCount, cnt)


print(finalCount)
