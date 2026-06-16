soma_positivos = 0
cont_positivos = 0
soma_negativos = 0
cont_negativos = 0

for i in range(100):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero > 0:
        soma_positivos += numero
        cont_positivos += 1
    elif numero < 0:
        soma_negativos += numero
        cont_negativos += 1

if cont_positivos > 0:
    media_positivos = soma_positivos / cont_positivos
else:
    media_positivos = 0

if cont_negativos > 0:
    media_negativos = soma_negativos / cont_negativos
else:
    media_negativos = 0

diferenca = cont_positivos - cont_negativos

print("\n--- Resultados ---")
print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de números negativos: {cont_negativos}")
print(f"Média dos números positivos: {media_positivos:.2f}")
print(f"Média dos números negativos: {media_negativos:.2f}")
print(f"Diferença entre positivos e negativos: {diferenca}")