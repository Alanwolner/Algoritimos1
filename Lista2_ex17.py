lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
  print("Os valores formam um triângulo")

  if lado1 == lado2  and lado2 == lado3:
    print("Triângulo Equilátero")

  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isósceles")

  else:
    print("Triângulio Escaleno")

else:
  print("Os valores não formam um triangulo")