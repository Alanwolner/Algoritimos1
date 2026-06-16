nomes = []
medias = []

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    media = float(input(f"Digite a média de {nome}: "))
    nomes.append(nome)
    medias.append(media)
soma = 0

for i in range(5):
    soma += medias[i]
media_geral = soma / 5
acima_media = 0

print("\n--- Notas dos Alunos ---")
for i in range(5):
    print(f"Aluno: {nomes[i]} | Média: {medias[i]}")
    if medias[i] > media_geral:
        acima_media += 1

print(f"\nMédia geral da turma: {media_geral:.2f}")
print(f"Quantidade de alunos acima da média: {acima_media}")