# Loay Mohamed
# Challeng 4:

matrix = input("Input your n*m matrix:")
#matrix = [[-3, 3, -2], [-1, 5, -1], [3, 5, -2]]
n = len(matrix)
m = len(matrix[0])
health = 1
# check and validate matrix dimensions:
if m == 0 or n == 0:
    print("Invalid Matrix with dimensions " + str(n) + " , " + str(m))
for i in range(n):
    if len(matrix[i]) != m:
        print("Invalid Matrix with dimensions " + str(n) + " , " + str(m))

if matrix[0][0] < 0:
    health = -1*matrix[0][0] + 1


def dungeon(currhealth, i, j):
    if currhealth + matrix[i][j] > 0:
        currhealth += matrix[i][j]
        if i == n-1 and j == m-1:
            return True

        if i >= n-1 and j < m-1:
            return dungeon(currhealth, i, j+1)
        if i < n-1 and j >= m-1:
            return dungeon(currhealth, i+1, j)

        return dungeon(currhealth, i, j+1) or dungeon(currhealth, i+1, j)
    else:
        return False


while True:
    if dungeon(health, 0, 0):
        break
    else:
        health += 1

print(health)
