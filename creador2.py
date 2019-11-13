#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import xlrd


def crear_row(nombre, dfn, dmn, dfe, dme, extra):
    validator_extra = ''
    if extra == 'c':
        validator_extra = ', Validators.pattern(this.emailPattern)'
    elif isinstance(extra, float):
        validator_extra = ', Validators.maxLength(%s)' % int(extra)
    elif extra == '-':
        validator_extra = ', Validators.minLength(12), Validators.maxLength(13)'
    elif extra == '_':
        validator_extra = ', Validators.minLength(18), Validators.maxLength(18)'
    elif extra[0] == 'e':
        crear_row(nombre + '_texto', dfn, dmn, dfe, dme, float(extra[1:]))
        validator_extra = ''
    elif extra == 'l':
        validator_extra = ''
    else:
        print(extra + 'no controlado')

    fn[nombre] = cambiar_valor(dfn, validator_extra)
    mn[nombre] = cambiar_valor(dmn, validator_extra)
    fe[nombre] = cambiar_valor(dfe, validator_extra)
    me[nombre] = cambiar_valor(dme, validator_extra)


def cambiar_valor(dfn, valor):
    dfn = dfn.strip()
    if dfn == 'ob':
        dfn = '[Validators.required%s]' % valor
    elif dfn == 'opc':
        dfn = '[]'
    else:
        dfn = None
    return dfn


def return_none(valor):
    if not valor:
        return None
    return valor


model = 'catalogos.dato'
pk = 1
fn = {}
fe = {}
mn = {}
me = {}
book = xlrd.open_workbook('toJson.xlsx')
sheet = book.sheet_by_index(0)
datos = [fn, fe, mn, me]
linea = 0
while True:
    crear_row(sheet.cell(linea, 0).value, sheet.cell(linea, 1).value, sheet.cell(linea, 2).value,
              sheet.cell(linea, 3).value, sheet.cell(linea, 4).value, sheet.cell(linea, 5).value)
    linea += 1
    if sheet.nrows == linea:
        break

with open('datos.json', 'w') as file:
    json.dump(datos, file, ensure_ascii=False, indent=2, separators=(", ", " : "))

print('end')
