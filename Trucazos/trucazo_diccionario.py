dic = {1: 1, 2: 200, 3: 30000}

elegidos = [1, 2]

"""
dic_elegidos = {}
for i in elegidos:  dic_elegidos[i] = dic[i]
"""
dic_elegidos = {i: dic[i] for i in elegidos if i in dic}
""" transcription for:
for i in elegidos:
    if i in dic:
        dic_elegidos[i] = dic[i]

"""

print(dic_elegidos)
