def encontrar_maximo(vetor):
    maximo = vetor[0]
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
    return maximo

def encontrar_minimo(vetor):
    minimo = vetor[0]
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento
    return minimo

vetor=[5,7,4,3]
print(encontrar_maximo(vetor))
print(encontrar_minimo(vetor))
