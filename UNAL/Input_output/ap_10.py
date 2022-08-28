c,k = int(input()),int(input())
p = ((k-c)/c)*100
res = f"Hubo una ganancia de $ {abs(k-c)} correspondiente al {abs(p)} % del capital invertido" if p>0 else f"Hubo una perdida de $ {abs(k-c)} correspondiente al {abs(p)} % del capital invertido" if p<0 else 'No hubo ni ganancia ni perdida, la inversion fue un desperdicio de tiempo, pero al menos no de dinero'
print(res)