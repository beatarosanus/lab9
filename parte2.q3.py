from random import randint

lista1 = [randint(0, 50) for i in range(20)]
lista2 = [randint(0, 50) for i in range(20)]

comum = list(set(lista1) & set(lista2))

comum.sort()

print("Primeira lista:", lista1)
print("Segunda lista:", lista2)
print("Valores repetidos:", comum)
