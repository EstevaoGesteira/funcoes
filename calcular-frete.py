def quilometro(km, expresso):
    if km <= 5 :
        print("Frete grátis.")
    elif km > 5 and km <=15:
        if expresso == True:
            print(f"O frete expresso custa: {8 * 1.5}")
        else:
            print("O frete custa 8 reais.")
    else:
        if expresso == True:
            print(f"O frete expresso custa: {15 * 1.5}")
        else:
            print("O frete custa 15 reais.")

km = int(input("Digite quantos km de distância: "))
expresso = input("Deseja frete expresso? (s/n): ")
if expresso == "s":
    expresso = True

quilometro(km, expresso)


