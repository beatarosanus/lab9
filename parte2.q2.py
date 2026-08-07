lista_a = []
lista_b = []

tam_a = int(input("Digite o tamanho da primeira lista: "))

for i in range(tam_a):
    lista_a.append(int(input("Número: ")))

tam_b = int(input("Digite o tamanho da segunda lista: "))

for i in range(tam_b):
    lista_b.append(int(input("Número: ")))

misturada = []

for pos in range(max(len(lista_a), len(lista_b))):
    if pos < len(lista_a):
        misturada += [lista_a[pos]]

    if pos < len(lista_b):
        misturada += [lista_b[pos]]

print("Resultado:", misturada)
