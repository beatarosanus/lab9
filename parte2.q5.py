numero = int(input("Informe o tamanho da matriz: "))

matriz = [
    [linha for coluna in range(numero)]
    for linha in range(numero)
]

print(matriz)
