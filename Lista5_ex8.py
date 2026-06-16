soma_dois_filhos = 0
cont_dois_filhos = 0

soma_sem_filhos = 0
cont_sem_filhos = 0

soma_um_filho = 0
cont_um_filho = 0

soma_geral = 0

for i in range(1):
    print(f"\nPessoa {i + 1}")

    nome = input("Digite o nome: ")
    salario = float(input("Digite o salário: R$ "))
    filhos = int(input("Digite o número de filhos: "))

    soma_geral += salario

    if filhos == 2:
        soma_dois_filhos += salario
        cont_dois_filhos += 1

    elif filhos == 0:
        soma_sem_filhos += salario
        cont_sem_filhos += 1

    elif filhos == 1:
        soma_um_filho += salario
        cont_um_filho += 1

if cont_dois_filhos > 0:
    media_dois_filhos = soma_dois_filhos / cont_dois_filhos
else:
    media_dois_filhos = 0

if cont_sem_filhos > 0:
    media_sem_filhos = soma_sem_filhos / cont_sem_filhos
else:
    media_sem_filhos = 0

if cont_um_filho > 0:
    media_um_filho = soma_um_filho / cont_um_filho
else:
    media_um_filho = 0

media_geral = soma_geral / 100


print("\n--- Resultados ---")
print(f"Salário médio de quem possui 2 filhos: R$ {media_dois_filhos:.2f}")
print(f"Salário médio de quem não possui filhos: R$ {media_sem_filhos:.2f}")

if media_um_filho > media_dois_filhos:
    print("A maior média salarial é das pessoas que possuem 1 filho.")
elif media_dois_filhos > media_um_filho:
    print("A maior média salarial é das pessoas que possuem 2 filhos.")
else:
    print("As médias salariais de 1 e 2 filhos são iguais.")

print(f"Salário médio geral: R$ {media_geral:.2f}")