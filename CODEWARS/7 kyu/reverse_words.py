def reverse_words(text:str):
    textos_invertidos = []
    for i in text.split(" "): textos_invertidos.append(i[-1:0:-1]+i[0]) if i != "" else 0

    invertidos = "".join(textos_invertidos)
    for i in range(len(text)):
        if text[i] == " " and invertidos[i] != " ":
            invertidos = invertidos[:i] + " " + invertidos[i:]
    
    return invertidos


text = "holasaurio"

'''
a = text[ 2: 5]

print(a)
'''

print(reverse_words('HABIA UNA VEZ UNA IGUANA'))