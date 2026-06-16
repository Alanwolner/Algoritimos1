Movimentações = []

while True:
  valor = float(input("Digite a movimentação (0 para encerrar): "))
  if valor == 0:
    break

  Movimentações.append(valor)

receitas = 0
despesas = 0

for i in range(len(Movimentações)):
  if Movimentações[i] > 0:
    receitas += Movimentações[i]
  else:
    despesas += Movimentações[i]

saldo = receitas + despesas
print("\n--- Relatorio ---")
print(f"Total arrecadado: R$ {receitas:.2f}")
print(f"Total gasto: R$ {despesas:.2f}")
print(f"Saldo final do dia: R$ {saldo:.2f}")

if saldo > 0:
    print("Situação: Lucro")
elif saldo < 0:
    print("Situação: Prejuízo")
else:
    print("Situação: Empate")