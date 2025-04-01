# Encontre o subarray contínuo com a maior soma dentro de um array de números inteiros.
def maior_soma_suberray(array):
    # Inicializa os valores de max_atual e max_global com o primeiro elemento
    max_atual = max_global = array[0]

    # Intera sobre o array a partir do segundo elemento 
    for i in range (1,lent(array)):
        max_atual = max(array[1], max_atual + array[1])
        max_global = max(max_global, max_atual)
        return max_global