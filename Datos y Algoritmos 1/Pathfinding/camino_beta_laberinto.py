def camino(laberinto, origen, destino):
    return f(laberinto,origen[1],origen[0],destino,0)
def f(l:list,x:int,y:int,d:list,c:int)-> int:
    if(x==d[1]and y ==d[0]): return c
    if(l[y][x]==0): return 999999
    l[y][x]= 0


    if(   x==0      and   y==0   ): return min(f(l,x+1,y,d,c+1),f(l,x,y+1,d,c+1))
    if(   x==0      and y==len(l)): return min(f(l,x+1,y,d,c+1),f(l,x,y-1,d,c+1))
    if(x==len(l[0]) and   y==0   ): return min(f(l,x-1,y,d,c+1),f(l,x,y+1,d,c+1))
    if(x==len(l[0]) and y==len(l)): return min(f(l,x-1,y,d,c+1),f(l,x,y-1,d,c+1))

    if(    x==0    ): return min(f(l,x+1,y,d,c+1),f(l,x,y-1,d,c+1),f(l,x,y+1,d,c+1))
    if(x==len(l[0])): return min(f(l,x-1,y,d,c+1),f(l,x,y-1,d,c+1),f(l,x,y+1,d,c+1))
    if(    y==0    ): return min(f(l,x-1,y,d,c+1),f(l,x+1,y,d,c+1),f(l,x,y+1,d,c+1))
    if(  y==len(l) ): return min(f(l,x-1,y,d,c+1),f(l,x+1,y,d,c+1),f(l,x,y-1,d,c+1))

    return min(f(l,x-1,y,d,c+1),f(l,x+1,y,d,c+1),f(l,x,y-1,d,c+1),f(l,x,y+1,d,c+1))


#print(return min(1,3,8,1,4,25,23,5,2,34,5,2,-124))
#        0  1  2  3  4  5  6  7  8  9
lab =  [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1], #0
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1], #1
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1], #2
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], #3
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1], #4
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], #5
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1], #6
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0], #7
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], #8
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]] #9
#print(len(lab[0]))
ini = [0,0]
fin = [7,5]
print(camino(lab,ini,fin))
#print(lab[4][6])