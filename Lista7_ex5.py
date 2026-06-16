votos = [1, 2, 3, 2, 2, 1, 3, 3, 2, 1, 2, 3, 2, 2, 1, 3, 3, 2, 1, 2]
ruim = 0
bom = 0
excelente = 0

for i in range(len(votos)):
    if votos[i] == 1:
        ruim += 1
    elif votos[i] == 2:
        bom += 1
    elif votos[i] == 3:
        excelente += 1

total = len(votos)

perc_ruim = (ruim / total) * 100
perc_bom = (bom / total) * 100
perc_excelente = (excelente / total) * 100

if ruim > bom and ruim > excelente:
    vencedor = "Ruim"
elif bom > ruim and bom > excelente:
    vencedor = "Bom"
elif excelente > ruim and excelente > bom:
    vencedor = "Excelente"
else:
    vencedor = "Houve empate"

print("\n--- Relatorio ---")
print(f"Ruim: {ruim} votos - {perc_ruim:.2f}%")
print(f"Bom: {bom} votos - {perc_bom:.2f}%")
print(f"Excelente: {excelente} votos - {perc_excelente:.2f}%")
print(f"Avaliação vencedora: {vencedor}")