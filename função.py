def calcular_desconto(valor, percentual):
    desconto = valor * percentual / 100
    return valor - desconto

preco_final = calcular_desconto(200,10)
print(preco_final)
