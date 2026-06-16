def depositar (saldo, valor):
  if valor > 0:
    saldo += valor
  else:
    print("Erro: o valor do deposito não pode ser negativo ou zero")
  return saldo
  
def sacar (saldo, valor):
  if valor <= 0:
    print("Erro: o valor do saque não pode ser negativo ou zero")
  elif valor > saldo:
    print("Erro: saldo insuficiente para realizar o saque.")
  else:
    saldo -= valor
  return saldo
    
saldo = 0

while True:
    print("--- Caixa Eletrônico ---")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      print(f"Seu salto atual é: R$ {saldo}")
    elif opcao == "2":
      valor = float(input("Digite o valor do deposito: "))
      saldo = depositar(saldo, valor)

    elif opcao == "3":
      valor = float(input("Digite o valor do saque: "))
      saldo = sacar(saldo, valor)

    elif opcao == "4":
      print("Encerrando o programa...")
      break

    else:
      print("Opção invalida! Tente novamente.")