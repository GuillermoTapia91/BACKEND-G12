personas = [
    {
        'nombre': 'Eduardo',
        'apellido': 'de"Rivero',
        'hobies': [
            {
                'nombre': 'montar bici',
                'dificultad': 'intermedio',
                'observaciones': ['Dolor de Rodilla', 'Cansancio', 'otra cosa']
            }
        ]
    },
    {
        # ...
    },
    {
        # ...
    }
]

print(personas[0]['hobies'][0]['observaciones'][0])
