#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import xlrd


def crear_row(persona, nombre, dfn, dmn, df, dfe, dme, extra):
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
        validator_extra = ', Validators.maxLength(%s)' % int(extra[1:])
    elif extra == 'l':
        validator_extra = ''
    else:
        print(extra + 'no controlado')

    dfn = cambiar_valor(dfn, validator_extra)
    dmn = cambiar_valor(dmn, validator_extra)
    df = cambiar_valor(df, validator_extra)
    dfe = cambiar_valor(dfe, validator_extra)
    dme = cambiar_valor(dme, validator_extra)

    if persona == 1:
        nfn[nombre] = dfn
        nmn[nombre] = dmn
        nfi[nombre] = df
        nfe[nombre] = dfe
        nme[nombre] = dme
        efn[nombre] = efn.get(nombre)
        emn[nombre] = emn.get(nombre)
        efi[nombre] = efi.get(nombre)
        efe[nombre] = efe.get(nombre)
        eme[nombre] = eme.get(nombre)
    else:
        efn[nombre] = dfn
        emn[nombre] = dmn
        efi[nombre] = df
        efe[nombre] = dfe
        eme[nombre] = dme
        nfn[nombre] = nfn.get(nombre)
        nmn[nombre] = nmn.get(nombre)
        nfi[nombre] = nfi.get(nombre)
        nfe[nombre] = nfe.get(nombre)
        nme[nombre] = nme.get(nombre)


def cambiar_valor(dfn, valor):
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
nfn = {}
nmn = {}
nfi = {}
nfe = {}
nme = {}
efn = {}
emn = {}
efi = {}
efe = {}
eme = {}
nacional = [nfn, nmn, nfi, nfe, nme]
extranjero = [efn, emn, efi, efe, eme]
book = xlrd.open_workbook('toJson.xlsx')
sheet = book.sheet_by_index(0)
datos = [nacional, extranjero]
linea = 0
while True:
    crear_row(sheet.cell(linea, 0).value, sheet.cell(linea, 1).value, sheet.cell(linea, 2).value,
              sheet.cell(linea, 3).value, sheet.cell(linea, 4).value, sheet.cell(linea, 5).value,
              sheet.cell(linea, 6).value, sheet.cell(linea, 7).value)
    linea += 1
    if sheet.nrows == linea:
        break

with open('datos.json', 'w') as file:
    json.dump(datos, file, ensure_ascii=False, indent=2, separators=(", ", " : "))

print('end')
