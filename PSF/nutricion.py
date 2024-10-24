
def nutricion(imc):
    if 18.5 <= imc <= 24.9:
        return "saludable"  # Clase CSS para color verde
    elif 25 <= imc <= 29.9:
        return "sobrepeso"  # Clase CSS para color naranja
    elif 30 <= imc <= 34.9:
        return "obesidad"  # Clase CSS para color rojo
    else:
        return "fuera_rango"  # Clase CSS para color gris





