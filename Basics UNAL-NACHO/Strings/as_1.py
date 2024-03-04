for _ in range(int(input())):
    s = input()[-2:]
    try: res = "Galo" if s == "ix" else "Romano" if s == "us" else "Godo" if s == "ic" else "Griego" if s == "as" else "Normando" if s == "af" else "Breton" if s in ["is","ax"] else "Hispano" if s == "ez" else "Indio" if s[-1] == "a" else "Desconocido"
    except: res = "Desconocido"
    print(res)