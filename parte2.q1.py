from random import randint

valores = [randint(-100, 100) for i in range(10)]

copia_ordenada = sorted(valores)

print("Lista ordenada:", copia_ordenada)
print("Lista original:", valores)

print("Posição maior:", valores.index(max(valores)))
print("Posição menor:", valores.index(min(valores)))
print("Total:", sum(valores))
print("Média:", sum(valores) / 10)
