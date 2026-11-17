def calcular_desconto(valor, percentual):
    return valor - valor * percentual/100
#Regra: Parâmetro padrão sempre no final do escopo da função

print(calcular_desconto(percentual=30,valor=80)) #Parametro nomeado
print(calcular_desconto(200, 15)) #170.00
print(calcular_desconto(200)) #180.00  #Parâmetro posicional
