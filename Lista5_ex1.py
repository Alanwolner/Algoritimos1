def celsius_para_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def metros_para_centimetros(metros):
  return metros * 100

while True:
  print("--- MENU DE CONVERSÃO ---")
  print("1 - Converter Celsius para Fahrenheit")
  print("2 - Converter metros para centímetros")
  print("3 - Sair")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"Resultado: conversão é igual a {fahrenheit}°F")

  elif opcao == "2":
    metros = float(input("Digite o valor em metros: "))
    centimetros = metros_para_centimetros(metros)
    print(f"A conversão é igual a {centimetros} cm")

  elif opcao == "3":
    print("Encerrando o programa...")
    break

  else:
    print("Opção invalida! Tente novamente.")