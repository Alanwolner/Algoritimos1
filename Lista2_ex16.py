tipo = input("Digite o tipo do bilhete (unitario, duplo ou 10 viagens): ")

if tipo == "unitario":
  preco = 1.30
elif tipo == "duplo":
  preco = 2.60
elif tipo == "10 viagens":
  preco = 12.00
else:
  print("Tipo de bilhete invalido.")
  exit ()

valor = float(input("Digite o valor pago: "))
quantidade = int(valor // preco)
troco = valor - (quantidade * preco)

print(f"Quantidade de bilhetes: {quantidade}")
print(f"Troco: R${troco: .2f}")