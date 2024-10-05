a, b = input(), input()
if a == b:
    print("empate")
elif (
    (a == "piedra" and b == "tijera")
    or (a == "tijera" and b == "papel")
    or (a == "papel" and b == "piedra")
):
    print(f"{a} vence {b}")
else:
    print(f"{b} vence {a}")
