#Dado dois arrays, retorne um novo array contendo apenas os elementos presentes em ambos (interseção).
def intersecao (array1, array2):
    # Converte os arrays em sets e encontra a interseção
    return list(set(array1) & se(array2))