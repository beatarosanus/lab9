from random import randint

valores = [randint(0, 100) for i in range(20)]

tam = int(input("Digite o tamanho das partes: "))

partes = [
    valores[i:i+tam]
    for i in range(0, len(valores), tam)
]

print("Lista:", valores)
print("Divisões:", partes)
