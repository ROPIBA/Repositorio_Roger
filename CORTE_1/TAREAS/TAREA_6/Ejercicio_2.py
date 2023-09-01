
meses = {
    "enero": 31,
    "febrero": 28,
    "marzo": 31,
    "abril": 30,
    "mayo": 31,
    "junio": 30,
    "julio": 31,
    "agosto": 31,
    "septiembre": 30,
    "octubre": 31,
    "noviembre": 30,
    "diciembre": 31
}

festivos = {
    "enero": "Año Nuevo",
    "febrero": "Día de San Valentín",
    "marzo": "Día de San José",
    "abril": "Semana Santa",
    "mayo": "Día del Trabajo",
    "junio": "Día de la Madre",
    "julio": "Día de la Independencia",
    "agosto": "Día del Trabajador",
    "septiembre": "Día de la Independencia de México",
    "octubre": "Día de la Raza",
    "noviembre": "Día de los Muertos",
    "diciembre": "Navidad"
}

mes = input("Introduce el nombre de un mes: ").lower()

if mes in meses:

    num_dias = meses[mes]
    
    festivo = festivos[mes]
    
    print(f"{mes.capitalize()} tiene {num_dias} días, y el festivo correspondiente es el {festivo}.")
else:
    print("Por favor, ingresa un mes válido.")
