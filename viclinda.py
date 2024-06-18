
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Exemplo de uso:
# numero = int(input("Digite um número para calcular o fatorial: "))
# resultado = calcular_fatorial(numero)
# print(f"O fatorial de {numero} é {resultado}")
