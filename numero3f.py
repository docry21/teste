# Definindo os dois primeiros números
sequencia = [2, 10]

# Adicionando os próximos elementos
for i in range(2, 7):
    # Multiplicando os dois últimos dígitos dos números antecedentes
    ultimo = sequencia[-1]
    penultimo = sequencia[-2]
    proximo = (ultimo % 10) * (penultimo % 10)
    sequencia.append(proximo)

# Adicionando o próximo número
ultimo = sequencia[-1]
penultimo = sequencia[-2]
proximo = (ultimo % 10) * (penultimo % 10)
sequencia.append(proximo)

print("A sequência completa é:", sequencia)
