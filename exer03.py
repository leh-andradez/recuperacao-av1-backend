#Receba um array de números e calcule a média aritmética dos valores.
def calcular_media(array):
    if len(array) == 0:
        return 0  # Caso o array esteja vazio, retornamos 0 para evitar erro de divisão por zero.
    return sum(array) / len(array)