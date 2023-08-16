z=input('ingrese (a) si quiere sar el programa del las letras, ingrese (b) si quiere usar el programa del IVA, ingrese (c) si quiere usar el programa de los trianglos :')
if z=='a':
    a = input("Ingrese una letra: ")

    if a.isalpha() and len(a) == 1:
        if a in 'aeiou':
         print("Es vocal.")
        else:
            print("Es consonante.")
    else:
            print("error, solo una letra.")
elif z=='b':
    a=eval(input('ingrese el tiempo (en minutos) que usó en el parqueadero: '))
    b=139*a #subtotal
    c=b*0.19 #IVA
    d=b+c #total
    e=((d + 49) // 50) * 50 # arreglo para pago
    print('Recibo de parqueadero\n''Tiempo:',a,' minutos' '\n' 'Subtotal: ',b, 'pesos' '\n' 'IVA: ',c, 'pesos' '\n' 'Total: ', e, 'pesos')
elif z=='c':
    def tipoT(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilatero"
            elif a == b or a == c or b == c:
                return "Isosceles"
            else:
                return "Escaleno"
        else:
            return "No se puede formar un triángulo"

    a = eval(input("poner la longitud del primer lado: "))
    b = eval(input("poner la longitud del segundo lado: "))
    c = eval(input("poner la longitud del tercer lado: "))

    TT = tipoT(a, b, c)
    print(f"El tipo de triángulo es: {TT}")
else:
    print('ERROR, solo se pede leer las letras a,b o c (en minuscula)')