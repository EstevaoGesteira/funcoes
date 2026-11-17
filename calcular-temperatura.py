def temp():
    celsius = float(input("Digite a temperatura em celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

print(f"A temperatura digitada em celsius, convertida em Fahrenheit é {temp()}")