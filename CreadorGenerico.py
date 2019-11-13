import json

import xlrd


class CrearFixture:
    model = 'inventario.UnidadCFDI'
    name_pk = 'clave'
    data = []
    book = None
    sheet = None
    linea = 0

    def __init__(self):
        self.book = xlrd.open_workbook('toJson.xlsx')
        self.sheet = self.book.sheet_by_index(0)

    def run(self):
        while True:
            self.data.append(
                {
                    'model': self.model,
                    'fields': {
                        'clave': str(self.sheet.cell(self.linea, 0).value),
                        'nombre': self.sheet.cell(self.linea, 1).value
                    }
                }
            )
            self.linea += 1
            if self.sheet.nrows <= self.linea:
                break

        with open('datos.json', 'w') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2, separators=(", ", " : "))


