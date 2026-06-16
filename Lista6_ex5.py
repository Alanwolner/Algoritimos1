A = []
B = []

for i in range(6):
    valorA = float(input(f"Digite o valor {i+1} da lista A: "))
    A.append(valorA)
    valorB = float(input(f"Digite o valor {i+1} da lista B: "))
    B.append(valorB)

for i in range(6):
    A[i] = A[i] + B[i]

print("Nova lista A:", A)