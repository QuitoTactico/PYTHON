

def dfs(matriz, x, y):
    matriz[x][y]  = 0
  
    n, m = len(matriz), len(matriz[0])
    for fila in (0, 1, -1):
        for col in (0, 1, -1):
            newx, newy = x + fila, y + col
            if 0 <= newx < n and 0 <= newy < m:
                if matriz[newx][newy] == 0:
                    continue
                dfs(matriz, newx, newy)

def islas(matriz):
  ans = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      if matriz[i][j] == 1:
        dfs(matriz, i, j)
        ans += 1
  return ans

M = [[1,1,0,0,0],[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,1,0,1]]

print(islas(M))