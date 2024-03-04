#conejo en matriz, hay manzanas y zanahorias
# que ande y llegue al borde del mapa
#  c | # | .
#  . | * | *
#  . | . | # 
# # zanahoria vale idk, 1
# * manzana vale idk, 3, siu
# probar rutas y ver cuantos puntos obtiene, básicamente

def sat(M,i,j,d,k):
 if M[i][j] == ".":
   return 0
 elif M[i][j] == "#":
   return k
 else:
   return d
 
def c(M,i,j,d,k):
 n = len(M)
 m = len(M[0])
 if i >= n or j >= m:
   return 0
 elif i == n-1 and j == m-1:
   return sat(M,i,j,d,k)
 else:
   return sat(M,i,j,d,k) + max(c(M,i,j+1,d,k),c(M,i+1,j,d,k))

def main():
#Qué!?
 m = [[".","#","."],
      [".","*","*"],
      [".",".","#"]
     ]
 print(c(m,0,0,3,1))
main()

def leer():
 linea0 = input()
 n,m = linea0.split(" ")
 n,m = int(n), int(m)
 linea1 = input()
 d,k = linea1.split(" ")
 d,k = int(d), int(k)
 arregloDeCadenas = [0]*n
 for i in range(n):
  arregloDeCadenas[i] = input()
  arregloDeCadenas[i] = arregloDeCadenas[i].split(" ")
 print(c(arregloDeCadenas,0,0,d,k))

leer()