def soma_valores():
    entrada = input("Digite um valor (ou pressione Enter para terminar): ")

    if entrada == "":
        return 0.0
    return float(entrada) + soma_valores()

# Programa principal
total = soma_valores()
print(f"Soma total = {total}")