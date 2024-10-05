thash = {}
basura_pa_que_existes_morite_ni_pa_input_sirves = input()
for i in list(map(int, input().split())):
    thash[i] = True

i = 1
while True:
    if i not in thash:
        print(i)
        quit()
    i -= -1  # JIJIJIJA
