def verifica(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False

# Solicita um número ao usuário
num = int(input("Digite um número: "))

# Verifica se o número pertence à sequência
if verifica(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
