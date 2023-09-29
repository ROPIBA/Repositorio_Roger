def recursiva(lista):
    if len(lista) == 1:
        return lista[0]
    
    maximo = recursiva(lista[1:])
    
    return max(lista[0], maximo)

lista_de_prueba = [16,58,63,21,1,64]
print(f'la lista de pruba: ',lista_de_prueba)
mayor = recursiva(lista_de_prueba)
print(f"El elemento más grande es: {mayor}")
 