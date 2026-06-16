for numero in range(2, 20001):
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(numero)