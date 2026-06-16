def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Digite o valor de n: "))
print(f"O {n}º termo da sequência de Fibonacci é {fibonacci(n)}")