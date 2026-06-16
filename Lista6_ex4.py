A = []

for i in range(8):
    valor = int(input(f"Digite o {i+1}º número inteiro: "))
    A.append(valor)

maior = A[0]
for i in range(8):
    if A[i] > maior:
        maior = A[i]

print(f"O maior valor da lista é: {maior}")