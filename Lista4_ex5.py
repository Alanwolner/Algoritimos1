def perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma = soma + i
    if soma == n:
        return 1
    else:
        return 0

numero = int(input("Digite um número: "))
resultado = perfeito(numero)
print(resultado)