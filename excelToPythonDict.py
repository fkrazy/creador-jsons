import xlrd


class ExcelToPythonDict:
    def run(self, path):
        data = ""
        book = xlrd.open_workbook(path)
        sheet = book.sheet_by_index(0)
        linea = 0
        while sheet.ncols > linea:
            nombre = sheet.cell(0, linea).value.lower().replace(" ", "_")
            if nombre != '':
                data += nombre + "= {\n"
            subnombre = sheet.cell(1, linea).value.lower().replace(" ", "_")
            data += f"'{subnombre}': sheet.cell(linea, {linea}).value,\n"
            linea += 1
            if sheet.ncols > linea:
                if sheet.cell(0, linea).value != '':
                    data += '}\n'
            else:
                data += '}\n'

        return data.replace(",\n}", "\n}")
