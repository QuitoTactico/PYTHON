
def factor_lorentz():
    v = float(input())
    cal = 1 / (1-((v**2)/(1079252848.8**2)))**0.5
    print(round(cal,15))

for i in range(int(input())): factor_lorentz()
