import json
import xlrd

model = 'catalogos.SeccionDocumento'


def crear_documento_fixture():

    def create_row(pk, seccion, descripcion):
        return {'model': model,
                'pk': int(pk),
                'fields': {
                    'descripcion': descripcion,
                    'seccion': int(seccion)
                }
                }
    data = []
    book = xlrd.open_workbook('documentosfixture.xlsx')
    sheet = book.sheet_by_index(0)
    linea = 0
    while True:
        data.append(create_row(sheet.cell(linea, 0).value, sheet.cell(linea, 1).value, sheet.cell(linea, 2).value))
        linea += 1
        if sheet.nrows == linea:
            break

    with open('datos.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2, separators=(", ", " : "))


def crear_documento_comportamiento():
    def cambiar_valor(val):
        val = val.strip().lower()
        if not val:
            return 0
        elif val == 'y':
            return 1
        elif val == 'x':
            return 2
        else:
            print(val + ' valor no controlado')

    def create_row_personas (vfn, vfe, vmn, vme, vf):
        fn = cambiar_valor(vfn)
        fe = cambiar_valor(vfe)
        mn = cambiar_valor(vmn)
        me = cambiar_valor(vme)
        f = cambiar_valor(vf)
        return [fn, mn, f, fe, me]

    def create_row():
        personas = []
        for i in range(5):
            mover_x = i * 5 + i + 1
            personas.append(
                create_row_personas(sheet.cell(linea, 1 + mover_x).value,
                                    sheet.cell(linea, 2 + mover_x).value,
                                    sheet.cell(linea, 3 + mover_x).value,
                                    sheet.cell(linea, 4 + mover_x).value,
                                    sheet.cell(linea, 5 + mover_x).value))
        return personas

    data = {}
    book = xlrd.open_workbook('comportamiento_documento.xlsx')
    sheet = book.sheet_by_index(0)
    linea = 1
    while True:
        data[int(sheet.cell(linea, 0).value)] = create_row()
        linea += 1
        if sheet.nrows == linea:
            break
    with open('datos.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2, separators=(", ", " : "))
    print('finish')

