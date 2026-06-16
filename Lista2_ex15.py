sistema = 0

for i in range(3):
    nota = float(input(f"Digite a {i+1}° nota: "))
    sistema += nota
calculo = sistema / 3
print(f"Sua média foi {calculo:.1f}")

if calculo < 3.0:
    print("Aluno reprovado!")
elif calculo < 7.0:
    exame = 12 - calculo
    print("Aluno em exame!")
    print(f"Você precisa tirar {exame:.1f} no exame para ser aprovado.")
else:
    print("Aluno aprovado!")