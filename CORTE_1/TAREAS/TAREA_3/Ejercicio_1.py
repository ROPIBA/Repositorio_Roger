def mostrar_divisores(numero):
    if numero == 0:
        print("Ningún número es divisible entre cero")
    elif numero < 0:
        print("Por favor, ingresa un número positivo.")
    else:
        divisores = [i for i in range(1, numero + 1) if numero % i == 0]
        print(f"Los divisores positivos de {numero} son: {divisores}")

try:
    numero = int(input("Ingresa un número: "))
    mostrar_divisores(numero)
except ValueError:
    print("Por favor, ingresa un número válido.")
