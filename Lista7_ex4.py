produtos = []

while True:
    preco = float(input("Digite o preço do produto (valor negativo para encerrar): "))
    if preco < 0:
        break
    produtos.append(preco)

valor_bruto = 0
for i in range(len(produtos)):
    valor_bruto += produtos[i]

quantidade = len(produtos)
if quantidade > 10:
    desconto = valor_bruto * 0.05
else:
    desconto = 0
valor_final = valor_bruto - desconto

print("--- Cupom de compra ---")
print(f"Quantidade de produtos: {quantidade}")
print(f"Valor bruto: R$ {valor_bruto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")