class estudiante:
    def __init__(self):
        self.__nombre=None
        self.__apellido=None
        self.__edad=None
        self.nacionalidad="Colombia"


    def setNombre(self,nombre:str):
        self.__nombre=nombre


    def getNombre(self):
        return self.__nombre


    def setApellido(self,apellido:str):
        self.__apellido=apellido



    def getApellido(self):
        return self.__apellido


    def setEdad(self,edad:str):
        self.__edad=edad


    def getEdad(self):
        return self.__edad




def main():
    est1= estudiante()
    est1.setNombre(input('nombre: '))
    est1.setApellido(input('apellido: '))
    est1.setEdad(input('edad: '))


    print(f'el estudiante {est1.getNombre()} {est1.getApellido()}' ,\
          f'tiene una edad de {est1.getEdad()}',\
            f'y su nacionalidad es de {est1.nacionalidad}')

if __name__=='__main__':
    main()