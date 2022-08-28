temp = int(input())
edad = int(input())
if (temp > 27) and (edad >= 18):
    plata = int(input())
    if plata > 5:
        print("Comprar helado cerveza")
    else:
        print("Lo sentimos estas pobre")
else:
    print("Lo sentimos juventud")