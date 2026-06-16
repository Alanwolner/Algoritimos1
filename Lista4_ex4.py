def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não existem raízes reais.")
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("Raiz x1 =", x1)
        print("Raiz x2 =", x2)

bhaskara(1, -5, 6)