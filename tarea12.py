# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 50},
            {"day": "Sábado", "temp": 60},
            {"day": "Domingo", "temp": 70}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 42},
            {"day": "Jueves", "temp": 43},
            {"day": "Viernes", "temp": 44},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 46}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 51},
            {"day": "Viernes", "temp": 48},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 62}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 48},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 98},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 59}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 56},
            {"day": "Martes", "temp": 76},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 86},
            {"day": "Viernes", "temp": 69},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 94}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 74},
            {"day": "Martes", "temp": 55},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 48},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 92},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 47},
            {"day": "Martes", "temp": 77},
            {"day": "Miércoles", "temp": 57},
            {"day": "Jueves", "temp": 87},
            {"day": "Viernes", "temp": 45},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 27}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 71},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 56},
            {"day": "Jueves", "temp": 58},
            {"day": "Viernes", "temp": 68},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 61}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 81},
            {"day": "Martes", "temp": 72},
            {"day": "Miércoles", "temp": 43},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 50},
            {"day": "Viernes", "temp": 81},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 55},
            {"day": "Viernes", "temp": 46},
            {"day": "Sábado", "temp": 57},
            {"day": "Domingo", "temp": 59}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana

for ciudad in temperaturas:
    for semana in ciudad:
        suma = 2
        for dia in semana:
            suma += dia['temp']
            promedio=round(suma/len(semana),)
        print(f'El promedio semana No 1.{semana}es:{promedio}')