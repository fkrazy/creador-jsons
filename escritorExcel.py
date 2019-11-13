import json

import xlrd


def escribir():
    model = 'main_app.municipio'

    def create_object(pk, **kwargs):
        return {'model': model,
                'pk': int(pk) + 1,
                'fields': {
                    'estado': kwargs.get('estado'),
                    'nombre': kwargs.get('nombre')
                }
                }
    data = []
    book = xlrd.open_workbook('generico.xlsx')
    sheet = book.sheet_by_index(0)
    linea = 0
    estado = ''
    while True:
        temp = sheet.cell(linea, 0).value
        if temp != '':
            estado = int(temp)
        nombre = sheet.cell(linea, 1).value
        data.append(
            create_object(linea, nombre=nombre, estado=estado)
        )
        linea += 1
        if sheet.nrows <= linea:
            break

    with open('datos.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2, separators=(", ", " : "))


