def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    divisores = calcular_divisores(numero)
    suma_divisores = sum(divisores)
    return suma_divisores == numero

def main():
    print("Calculadora de Números Perfectos")
    cantidad_perfectos = int(input("Ingrese la cantidad de números perfectos que desea encontrar (máximo 10): "))
    
    if cantidad_perfectos > 10:
        cantidad_perfectos = 10
    
    encontrados = 0
    numero = 2  # Empezamos desde 2, ya que 1 no se considera un número perfecto
    
    while encontrados < cantidad_perfectos:
        if es_numero_perfecto(numero):
            print(f"Número perfecto encontrado: {numero}")
            encontrados += 1
        numero += 1

if __name__ == "__main__":
    main()

