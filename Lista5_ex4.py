def verificar_par_impar(valor):
    if valor % 2 == 0:
        return 1
    else:
        return 0

numero = int(input("Digite um número inteiro: "))
resultado = verificar_par_impar(numero)
if resultado == 1:
    print("O número é par.")
else:
    print("O número é ímpar.")