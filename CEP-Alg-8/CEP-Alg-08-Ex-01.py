def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número inteiro positivo: "))
print(f"{numero}! = {fatorial(numero)}")