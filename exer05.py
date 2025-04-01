#Dado um array de números inteiros, conte quantos são pares e quantos são ímpares.
def contar_pares_impares(array):
    pares = 0
    impares = 0

    for num in array:
        if num % 2 == 0:
            pares += 1
            else:
                impares += 1

                return pares,impares