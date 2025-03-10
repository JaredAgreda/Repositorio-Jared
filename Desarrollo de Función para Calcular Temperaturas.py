def calcular_promedio_por_ciudad(temperaturas, ciudades):
    promedios_ciudades = {}  # Diccionario para almacenar los promedios

    # Recorremos cada ciudad en la lista de temperaturas
    for i, ciudad in enumerate(temperaturas):
        nombre_ciudad = ciudades[i]  # Obtenemos el nombre de la ciudad correspondiente
        total_temperaturas = 0  # Inicializamos la suma total de temperaturas para la ciudad
        total_dias = 0  # Inicializamos el contador de días para la ciudad

        # Recorremos cada semana dentro de la ciudad
        for semana in ciudad:
            total_temperaturas += sum(dia["temp"] for dia in semana)  # Sumamos todas las temperaturas de la semana
            total_dias += len(semana)  # Contamos la cantidad total de días en la semana

        # Calculamos el promedio dividiendo la suma total por la cantidad de días
        promedio = total_temperaturas / total_dias
        promedios_ciudades[nombre_ciudad] = round(promedio, 2)  # Guardamos el promedio redondeado en el diccionario

    return promedios_ciudades  # Retornamos el diccionario con los promedios

# Lista de ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Datos de temperatura
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"dia": "Lunes", "temp": 18},
            {"dia": "Martes", "temp": 20},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 21},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 17},
            {"dia": "Martes", "temp": 19},
            {"dia": "Miércoles", "temp": 21},
            {"dia": "Jueves", "temp": 20},
            {"dia": "Viernes", "temp": 22},
            {"dia": "Sábado", "temp": 24},
            {"dia": "Domingo", "temp": 26}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 16},
            {"dia": "Martes", "temp": 18},
            {"dia": "Miércoles", "temp": 20},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 21},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 24}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 19},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 23}
        ]
    ],
    [   # Guayaquil
        [
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 31},
            {"dia": "Viernes", "temp": 33},
            {"dia": "Sábado", "temp": 35},
            {"dia": "Domingo", "temp": 36}
        ],
        [
            {"dia": "Lunes", "temp": 27},
            {"dia": "Martes", "temp": 29},
            {"dia": "Miércoles", "temp": 31},
            {"dia": "Jueves", "temp": 30},
            {"dia": "Viernes", "temp": 32},
            {"dia": "Sábado", "temp": 34},
            {"dia": "Domingo", "temp": 35}
        ],
        [
            {"dia": "Lunes", "temp": 26},
            {"dia": "Martes", "temp": 28},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 29},
            {"dia": "Viernes", "temp": 31},
            {"dia": "Sábado", "temp": 33},
            {"dia": "Domingo", "temp": 34}
        ],
        [
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 27},
            {"dia": "Miércoles", "temp": 29},
            {"dia": "Jueves", "temp": 28},
            {"dia": "Viernes", "temp": 30},
            {"dia": "Sábado", "temp": 32},
            {"dia": "Domingo", "temp": 33}
        ]
    ],
    [   # Cuenca
        [
            {"dia": "Lunes", "temp": 12},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 16},
            {"dia": "Jueves", "temp": 15},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 20}
        ],
        [
            {"dia": "Lunes", "temp": 11},
            {"dia": "Martes", "temp": 13},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 14},
            {"dia": "Viernes", "temp": 16},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 19}
        ],
        [
            {"dia": "Lunes", "temp": 10},
            {"dia": "Martes", "temp": 12},
            {"dia": "Miércoles", "temp": 14},
            {"dia": "Jueves", "temp": 13},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 17},
            {"dia": "Domingo", "temp": 18}
        ],
        [
            {"dia": "Lunes", "temp": 9},
            {"dia": "Martes", "temp": 11},
            {"dia": "Miércoles", "temp": 13},
            {"dia": "Jueves", "temp": 12},
            {"dia": "Viernes", "temp": 14},
            {"dia": "Sábado", "temp": 16},
            {"dia": "Domingo", "temp": 17}
        ]
    ]
]

# Calcular los promedios y mostrar resultados
promedios = calcular_promedio_por_ciudad(temperaturas, ciudades)
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio en {ciudad}: {promedio}°C")
