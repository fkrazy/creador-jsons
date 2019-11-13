import json

import xlrd


class ExcelByArbol:
    book = None
    sheet = None
    linea = 1
    data = []

    def __init__(self):
        self.book = xlrd.open_workbook('generico.xlsx')
        self.sheet = self.book.sheet_by_index(0)

    def crear_arbol(self):
        sheet = self.sheet
        linea = self.linea
        parent = None
        level = 0
        arboles = []
        tree = 0
        nivel_anterior = None
        # create tree
        while True:
            nombre = sheet.cell(linea, 2).value
            nivel = sheet.cell(linea, 0).value
            nivel = None if nivel == '' else int(nivel)
            codigo = sheet.cell(linea, 1).value
            nodo = Nodo(id=linea, nombre=nombre, codigo_base=nivel, codigo_agrupador=codigo)
            codigo = float(codigo)
            if not nivel and codigo - int(codigo) == 0:
                tree += 1
                nodo.data['level'] = 0
                parent = nodo
                arboles.append(nodo)
                level = 0
            elif not nivel:
                nodo.data['parent'] = arboles[-1]
                nodo.data['level'] = 1
                nodo.data['parent'].children.append(nodo)
                parent = nodo
                level = nodo.data['level']

            elif not nivel_anterior:
                level += 1
                nodo.data['level'] = level
                nodo.data['parent'] = parent
                parent.add_children(nodo)
            elif nivel_anterior < nivel:
                level += 1
                nodo.data['level'] = level
                parent = parent.children[-1]
                nodo.data['parent'] = parent
                parent.add_children(nodo)
            elif nivel_anterior > nivel:
                level -= 1
                nodo.data['level'] = level
                parent = parent.data['parent']
                nodo.data['parent'] = parent
                parent.add_children(nodo)
            else:
                nodo.data['level'] = level
                nodo.data['parent'] = parent
                parent.add_children(nodo)

            nodo.data['tree_id'] = tree
            nivel_anterior = nivel
            linea += 1
            if sheet.nrows <= linea:
                break
        for arbol in arboles:
            self.recorrer(arbol)
        self.data = sorted(self.data, key=lambda k: k['pk'])
        with open('datos.json', 'w') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=2, separators=(", ", " : "))

    def recorrer(self, nodo, count=0):
        count += 1
        nodo.data['lft'] = count
        for child in nodo.children:
            count = self.recorrer(child, count)
        rght = count + 1
        nodo.data['rght'] = rght
        self.data.append(nodo.object)
        return rght


class Nodo:
    data = {}
    children = None
    model = 'contabilidad.catalogocuentacontable'

    def __init__(self, **kwargs):
        self.children = []
        self.data = {
            'id': kwargs.get('id'),
            'nombre': kwargs.get('nombre'),
            'codigo_base': kwargs.get('codigo_base'),
            'level': kwargs.get('level'),
            'lft': kwargs.get('lft'),
            'rght': kwargs.get('rght'),
            'tree_id': kwargs.get('tree_id'),
            'parent': kwargs.get('parent'),
            'codigo_agrupador': kwargs.get('codigo_agrupador')
        }

    def add_children(self, child):
        self.children.append(child)

    @property
    def object(self, **kwargs):
        data = self.data
        parent_id = data.get('parent').data.get('id') if data.get('parent') else None
        return {'model': self.model,
                'pk': data.get('id'),
                'fields': {
                    'nombre': data.get('nombre'),
                    'codigo_base': data.get('codigo_base'),
                    'codigo_agrupador': data.get('codigo_agrupador'),
                    'parent_id': parent_id,
                    'lft': data.get('lft'),
                    'level': data.get('level'),
                    'tree_id': data.get('tree_id'),
                    'rght': data.get('rght')
                }
                }
