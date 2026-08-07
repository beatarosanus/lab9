frase = input("Digite uma frase: ")

indices = []

for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        indices.append(i)

print("Índices das vogais:", ", ".join(map(str, indices)))
print("Total:", len(indices), "vogais")
