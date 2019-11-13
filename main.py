from CreadorGenerico import CrearFixture
from documentosCreador import crear_documento_fixture, crear_documento_comportamiento
from escritorExcel import escribir
from excel_by_arbol import ExcelByArbol

print('elija una opcion')
decision = input()
while not (decision == 'exit' or decision == 'e'):
    if decision == '1':
        crear_documento_fixture()
    if decision == '2':
        crear_documento_comportamiento()
    if decision == '3':
        CrearFixture().run()
    if decision == '4':
        escribir()
    if decision == '5':
        creador = ExcelByArbol()
        creador.crear_arbol()
    print('elija una opcion')
    decision = input()
