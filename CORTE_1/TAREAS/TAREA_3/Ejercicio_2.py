num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

product = 0
counter = abs(num2)

while counter > 0:
    product += num1
    counter -= 1

if num2 < 0:
    product = -product

print(f"El producto de {num1} y {num2} es: {product}")
