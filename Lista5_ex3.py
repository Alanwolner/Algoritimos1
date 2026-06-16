def verificar_numero(valor):
  if valor >= 0:
    return 1
  else:
    return -1
  
numero = int(input("Digite um número inteiro: "))
resultado = verificar_numero(numero)

if resultado == 1:
  print("O numero é positivo")
else:
  print("O numero é negativo")