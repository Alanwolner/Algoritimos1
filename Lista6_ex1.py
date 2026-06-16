numeros = []
pares = []
impares = []

for i in range (6):
  valor = int(input(f"Digite o {i+1}° número: "))
  numeros.append(valor)

  if valor %2 == 0:
    pares.append(valor)
  else:
    impares.append(valor)

print(f"A quantidade de números pares: {len(pares)}")
print(f"Números pares: {pares}")

print(f"A quantidade de números impares: {len(impares)}")
print(f"Números impares: {impares}")
