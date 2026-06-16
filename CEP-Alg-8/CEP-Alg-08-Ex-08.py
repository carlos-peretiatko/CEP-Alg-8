def dec_para_bin(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    return dec_para_bin(n // 2) + str(n % 2)

numero = int(input("Digite um número inteiro não negativo: "))

if numero < 0:
    print("Erro: o valor deve ser um inteiro não negativo.")
else:
    print(f"Representação binária: {dec_para_bin(numero)}")