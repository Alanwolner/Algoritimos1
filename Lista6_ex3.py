logica = []
linguagem = []
iguais = []

for i in range(10):
    matricula = int(input(f"Digite a matrícula do {i+1}º aluno de Lógica: "))
    logica.append(matricula)

for i in range(8):
    matricula = int(input(f"Digite a matrícula do {i+1}º aluno de Linguagem de Programação: "))
    linguagem.append(matricula)

for matricula in logica:
    if matricula in linguagem:
        iguais.append(matricula)

print("\nAlunos que cursam as duas disciplinas:")
print(iguais)