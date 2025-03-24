# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Barcelona"

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0964782643"  # Agregar un número de teléfono

# Eliminar la clave "edad" del diccionario
    del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)