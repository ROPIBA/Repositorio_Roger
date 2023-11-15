class Ciu:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def tarea(self, tarea):
        return f"{self.nombre} está realizando la tarea: {tarea}"

class Med(Ciu):
    def __init__(self, nombre, edad, especialidad, hospital):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        self.hospital = hospital

    def tarea(self, tarea):
        return f"El médico {self.nombre} está realizando la tarea médica: {tarea}"

class Prof(Ciu):
    def __init__(self, nombre, edad, asignatura, colegio):
        super().__init__(nombre, edad)
        self.asignatura = asignatura
        self.colegio = colegio

    def tarea(self, tarea):
        return f"El profesor {self.nombre} está enseñando la materia {self.asignatura} como parte de la tarea: {tarea}"

class Ing(Ciu):
    def __init__(self, nombre, edad, campo, empresa):
        super().__init__(nombre, edad)
        self.campo = campo
        self.empresa = empresa

    def tarea(self, tarea):
        return f"El ingeniero {self.nombre} está aplicando sus conocimientos en el campo {self.campo} para llevar a cabo la tarea: {tarea}"

def menu():
    while True:
        print("1. Crear un médico")
        print("2. Crear un profesor")
        print("3. Crear un ingeniero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del médico: ")
            edad = input("Ingrese la edad del médico: ")
            especialidad = input("Ingrese la especialidad del médico: ")
            hospital = input("Ingrese el hospital del médico: ")
            medico = Med(nombre, edad, especialidad, hospital)
            tarea_medica = input("Ingrese una tarea médica para que el médico la realice: ")
            print(medico.tarea(tarea_medica))
        elif opcion == "2":
            nombre = input("Ingrese el nombre del profesor: ")
            edad = input("Ingrese la edad del profesor: ")
            asignatura = input("Ingrese la asignatura del profesor: ")
            colegio = input("Ingrese el colegio del profesor: ")
            profesor = Prof(nombre, edad, asignatura, colegio)
            tarea_enseñanza = input("Ingrese una tarea de enseñanza para que el profesor la realice: ")
            print(profesor.tarea(tarea_enseñanza))
        elif opcion == "3":
            nombre = input("Ingrese el nombre del ingeniero: ")
            edad = input("Ingrese la edad del ingeniero: ")
            campo = input("Ingrese el campo del ingeniero: ")
            empresa = input("Ingrese la empresa del ingeniero: ")
            ingeniero = Ing(nombre, edad, campo, empresa)
            tarea_ingenieria = input("Ingrese una tarea de ingeniería para que el ingeniero la realice: ")
            print(ingeniero.tarea(tarea_ingenieria))
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == '__main__':
    menu()
