#Implemente um algoritmo para ordenar um array de números em ordem crescente.
def ordenaçao_insercao(array):
    #Percorre o array apartir do segundo elemento
    for i in range(1,len(array)):
        chave = array[i]
        j = i - 1
        # Move os elementos do array que são maiores que a chave
        while j >=0 and array[j] >chave:
            array [j + 1] = array[j]
            j -= 1
         array[j + 1] = chave
    return array