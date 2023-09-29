def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def determinar_estado(imc):
    if imc < 18.5:
        return "Bajo peso"
    if imc < 24.9:
        return "Peso saludable"
    if imc < 29.9:
        return "Sobrepeso"
    return "Obesidad"

# Datos de las personas
personas = [
    ("Pedro Caceres", 188, 97),
    ("Maria Pérez", 160, 47),
    ("Julian Dominguez", 158, 58),
    ("Jessica Fuentes", 170, 73)
]

for nombre, peso, altura in personas:
    imc_resultado = calcular_imc(peso, altura)
    estado = determinar_estado(imc_resultado)
    print(f"{nombre}:")
    print(f"IMC: {imc_resultado:.2f}")
    print(f"Estado IMC: {estado}\n")
