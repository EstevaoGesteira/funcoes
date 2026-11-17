def calcular_media(n1,n2,n3):
    return (n1 + n2 + n3) / 3

def situacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

print(situacao(calcular_media(7,5,9)))