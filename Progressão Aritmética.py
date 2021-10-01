pt = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
dec = pt + (10-1) * raz
for c in range(pt, dec + raz, raz):
    print(c)