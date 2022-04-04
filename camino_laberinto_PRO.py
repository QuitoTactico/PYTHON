def camino(laberinto, origen, destino):
    zero = [0] * len(laberinto)
    laberinto.insert(0,zero)
    laberinto.append(zero)
    sol = f(zw(laberinto,len(laberinto)-1),origen[0]+1,origen[1]+1,destino,0)
    return -1 if sol == 999999 else sol
def f(l:list,y:int,x:int,d:list,c:int)-> int:
    if(l[y][x]==0): return 999999
    if(x==d[1]+1 and y ==d[0]+1): return c
    l[y][x]= 0
    return min(f(l,y+1,x,d,c+1),f(l,y,x+1,d,c+1),f(l,y-1,x,d,c+1),f(l,y,x-1,d,c+1))
def zw(l,i):
    l[i].insert(0,0)
    l[i].append(0)
    return l if(i==0) else zw(l,i-1)   #RETURN TERNARIO
    '''if(i==0):return l
    return zw(l,i-1)'''


       # 0  1  2  3  4  5  6  7  8  9
l =    [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1], #0
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1], #1
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1], #2
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], #3
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1], #4
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], #5
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1], #6
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0], #7
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], #8
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]] #9

ll = [[1,1,1],
      [0,1,1],
      [0,1,1]]





print(camino(ll,[0,0],[2,2]))  #importante#
