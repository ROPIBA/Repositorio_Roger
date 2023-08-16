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