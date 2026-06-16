def dec_bin_iterativo(q):
    result = ""

    while True:
        r = q % 2
        result = str(r) + result
        q = q // 2

        if q == 0:
            break

    return result

numero = int(input("Digite um número decimal: "))
print(f"Binário: {dec_bin_iterativo(numero)}")