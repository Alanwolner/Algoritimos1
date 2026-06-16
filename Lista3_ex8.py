n = int(input("Digite a quantidade de números: "))

soma_pares = 0
soma_impares = 0
quantidade_pares = 0
quantidade_impares = 0

for i in range(n):
  numero = int(input(f"Digite o {i+1}° número: "))

if numero %2 == 0:
  soma_pares += numero
  quantidade_pares += 1
else:
  soma_impares += numero
  quantidade_impares += 1

print(f"Soma dos números pares: {soma_pares}")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
print(f"Quantidade de ímpares: {quantidade_impares}")