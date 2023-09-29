import random

def leer():
    a = open('Alimentos.txt', 'rt')
    alimentos = a.readlines()
    a.close()
    save = []
    for i in alimentos[1:]:
        save.append(i.strip().split(','))
    return save

def precio_alimentos():
    return round(random.uniform(1000, 50000), 2)

def menu(nombre, lista_alimentos):
    for alimento in lista_alimentos:
        if alimento[1].lower() == nombre.lower():
            return alimento

def main():
    lista_alimentos = leer()
    nombre_alimento = input("Ingrese el nombre del alimento: ")
    
    alimento = menu(nombre_alimento, lista_alimentos)
    
    if alimento:
        valor_aleatorio = precio_alimentos()
        iva = float(alimento[2])
        precio_con_iva = round(valor_aleatorio * (1 + iva), 2)
        print(f"Nombre: {alimento[1]}")
        print(f"Valor: ${valor_aleatorio:.2f}")
        print(f"IVA: {iva}")
        print(f"Precio con IVA en pesos colombianos: ${precio_con_iva:.2f}")
    else:
        print(f"No se encontró el alimento: {nombre_alimento}")

if __name__ == '__main__':
    main()
