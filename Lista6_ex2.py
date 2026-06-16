numeros = []
multiplos2 = []
multiplos3 = []

for i in range (8):
  valor = int(input(f"Digite o {i+1}° número inteiro: "))
  numeros.append(valor)

  if valor %2 == 0:
    multiplos2.append(valor)

  if valor %3 == 0:
    multiplos3.append(valor)

print(f"Números multiplos de 2: {multiplos2}")
print(f"Números multiplos de 3: {multiplos3}")