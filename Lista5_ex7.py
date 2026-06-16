numeros = []
while True:
    valor = int(input("Digite um número: "))
    numeros.append(valor)
    opcao = input("Deseja continuar? (s/n): ")
    if opcao == "n":
        break

media = sum(numeros) / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"Média dos números: {media}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")