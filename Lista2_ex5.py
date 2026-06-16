maior_100 = 0

for i in range (5):
  numeros = int(input("Digite cinco números: "))
  if numeros > 100:
    maior_100 +=1

print(f"{maior_100} são maiores que 100.")