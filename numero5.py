string = "O rato roeu a roupa do rei de Roma"

# Inicializa a string invertida como uma string vazia
invertida = ""

# Inverte a string
for i in range(len(string)-1, -1, -1):
    invertida += string[i]

# Exibe a string invertida na tela
print(invertida)
