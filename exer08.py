#Desloque todos os elementos de um array para a direita (ou esquerda)
def deslocar_direita(array):
    in len(array) == 0:
        return array
    # O último elemnto
    ultimo = array [-1]
    # Desloca os elementos uma posição para a direita
    for i in range(len(array) - 1,0,-1):
        array[1] = array[i - 1]
    # Coloca o último elemento na primeira posição
    array[0] = ultimo
    return array        