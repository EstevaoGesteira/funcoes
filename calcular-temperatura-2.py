def celsius_para_fahrenheit(celsius):
    return (celsius * 1.8) + 32

temperatura = float(input("Temperatura em Celsius: "))
print(f"{temperatura}° = {celsius_para_fahrenheit(temperatura)}°F")

#Professor