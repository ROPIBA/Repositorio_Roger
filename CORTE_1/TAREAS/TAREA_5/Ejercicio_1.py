import math

def calcular_modulo(x, y):
    return math.sqrt(x**2 + y**2)

def calcular_componentes_rectangulares(x1, y1, x2, y2):
    componente_x = x2 - x1
    componente_y = y2 - y1
    return componente_x, componente_y

def main():
    print("Calculadora de Vectores")
    
    x1 = float(input("Ingrese la coordenada x del origen del vector: "))
    y1 = float(input("Ingrese la coordenada y del origen del vector: "))
    x2 = float(input("Ingrese la coordenada x del fin del vector: "))
    y2 = float(input("Ingrese la coordenada y del fin del vector: "))
    
    modulo = calcular_modulo(x2 - x1, y2 - y1)
    componente_x, componente_y = calcular_componentes_rectangulares(x1, y1, x2, y2)
    
    print("\nResultados:")
    print(f"Módulo del vector: {modulo:.2f}")
    print(f"Componente x: {componente_x:.2f}")
    print(f"Componente y: {componente_y:.2f}")

if __name__ == "__main__":
    main()
