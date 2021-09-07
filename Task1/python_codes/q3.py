# Loay Mohamed
# Challeng 3:

matrix = input("Input your m*n matrix:")
# matrix = [[1, 2], [3, 4]]
# matrix = [[7, 7], [7, 7]]
# matrix = [[7, 3, 6], [1, 4, 5], [9, 8, 2]]
# matrix = [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]]
m = len(matrix)
n = len(matrix[0])
# mapping from value to index..
mp = {}
for i in range(m):
    for j in range(n):
        mp.setdefault(matrix[i][j], []).append((i, j))


def find(p):
    if p != parent[p]:
        parent[p] = find(parent[p])
    return parent[p]


rank = [0]*(m+n)
ans = [[0]*n for _ in range(m)]

for k in sorted(mp):  # from minimum to maximum
    parent = list(range(m+n))
    for i, j in mp[k]:
        ii, jj = find(i), find(m+j)  # find
        parent[ii] = jj  # union
        rank[jj] = max(rank[ii], rank[jj])  # max rank

    seen = set()
    for i, j in mp[k]:
        ii = find(i)
        if ii not in seen:
            rank[ii] += 1
        seen.add(ii)
        rank[i] = rank[m+j] = ans[i][j] = rank[ii]

print(ans)
