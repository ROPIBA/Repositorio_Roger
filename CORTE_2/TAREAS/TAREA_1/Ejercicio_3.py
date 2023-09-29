def coinsidencias(a, b):
    posiciones = []
    lugar = 0

    while lugar < len(a):
        lugar = a.find(b, lugar)
        if lugar == -1:
            break
        posiciones.append(lugar)
        lugar += 1

    return posiciones

def main():
    a = input('Ingrese strings base con espacios entremedios: ')
    b = input('Ingrese otro string repetido: ')
    posiciones = coinsidencias(a, b)
    print(f'la considencia esta en la posicion: ',posiciones,'de la string base')

if __name__ == '__main__':
    main()

