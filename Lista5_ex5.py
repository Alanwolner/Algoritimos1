def receber ():
  cofre = []
  for i in range (3):
    v = int(input("Digite três valores inteiros: "))
    cofre.append(v)
  return cofre

valores = receber()
valores.sort()
print(valores)

