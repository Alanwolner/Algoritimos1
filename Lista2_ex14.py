sistema = 0

for i in range (3):
  notas = float(input(f"Digite a {i+1}° nota = "))
  sistema += notas
calculo = sistema/3

if calculo >= 8.1 and calculo <=10.0:
    print(f"Sua média final é {calculo: .1f} e seu conceito é A")
elif calculo >= 7.1 and calculo <=8.0:
    print(f"Sua média final é {calculo: .1f} e seu conceito é B")
elif calculo >=6.1 and calculo <=7.0:
    print(f"Sua média final é {calculo: .1f} e seu conceito é C")
elif calculo >= 5.1 and calculo <=6.0:
    print(f"Sua média final é {calculo: .1f} e seu conceito é D")
elif calculo >= 0.0 and calculo <=5.0:
    print(f"Sua média final é {calculo: .1f} e seu conceito é E")
else:
    print("Notas inseridas incorretamente. Tente novamente.")

  