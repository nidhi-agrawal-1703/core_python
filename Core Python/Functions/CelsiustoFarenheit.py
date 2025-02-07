def celsius_to_farenheit(celsius):
    farenheit=(celsius*9)/5 + 32
    return farenheit

c=float(input("Enter temperature in degree Celsius"))
print("Temperature in farenheit is",celsius_to_farenheit(c))
