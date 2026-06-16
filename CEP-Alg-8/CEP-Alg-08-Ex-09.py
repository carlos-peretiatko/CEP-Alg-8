def raiz_quadrada(n, estimativa=1.0):
    if abs(estimativa**2 - n) <= 1e-12:
        return estimativa

    nova_estimativa = (estimativa + n / estimativa) / 2

    return raiz_quadrada(n, nova_estimativa)


valores = [2, 9, 16, 25, 100]

for valor in valores:
    print(f"√{valor} ≈ {raiz_quadrada(valor)}")