import string

def palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())

    if len(texto) <= 1:
        return True

    if texto[0] != texto[-1]:
        return False

    return palindromo(texto[1:-1])

frase = input("Digite uma palavra ou frase: ")

if palindromo(frase):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")