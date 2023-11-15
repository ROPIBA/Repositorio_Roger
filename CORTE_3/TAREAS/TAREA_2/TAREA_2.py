class Art:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_precio(self, precio):
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def calcular_precio_total(self):
        return self._precio

class Art0IVA(Art):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._iva = 0

    def calcular_precio_total(self):
        return super().calcular_precio_total() * (1 + self._iva) + 5

class Art5IVA(Art):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._iva = 0.05

    def calcular_precio_total(self):
        return super().calcular_precio_total() * (1 + self._iva) + (0.1 * self._precio)

class Art19IVA(Art):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self._iva = 0.19

    def calcular_precio_total(self):
        return super().calcular_precio_total() * (1 + self._iva)

def menu():
    while True:
        print("1. Crear un artículo con 0% de IVA")
        print("2. Crear un artículo con 5% de IVA")
        print("3. Crear un artículo con 19% de IVA")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del artículo: ")
            precio = float(input("Ingrese el precio del artículo: "))
            articulo = Art0IVA(nombre, precio)
            print(f"Has creado el artículo {articulo.get_nombre()} con un precio total de {articulo.calcular_precio_total()}")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del artículo: ")
            precio = float(input("Ingrese el precio del artículo: "))
            articulo = Art5IVA(nombre, precio)
            print(f"Has creado el artículo {articulo.get_nombre()} con un precio total de {articulo.calcular_precio_total()}")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del artículo: ")
            precio = float(input("Ingrese el precio del artículo: "))
            articulo = Art19IVA(nombre, precio)
            print(f"Has creado el artículo {articulo.get_nombre()} con un precio total de {articulo.calcular_precio_total()}")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == '__main__':
    menu()
