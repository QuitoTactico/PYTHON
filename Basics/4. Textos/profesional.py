n = input()
print(n[18:(n.find("<",19,len(n)))] + n[n.find("tname'>")+7:n.find("<",n.find("tname'>")+7,len(n))])