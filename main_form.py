from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

import sys

from CreadorGenerico import CrearFixture
from documentosCreador import crear_documento_fixture, crear_documento_comportamiento
from escritorExcel import escribir
from excel_by_arbol import ExcelByArbol


class Dialog(QDialog):
    decision = 0
    NumGridRows = 3
    NumButtons = 4
    formGroupBox = None

    def __init__(self):
        super(Dialog, self).__init__()
        self.create_form_group_box()

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.formGroupBox)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

        self.setWindowTitle("Creador Fixtures")

    def accept(self):
        decision = self.decision
        if decision == 1:
            crear_documento_fixture()
        if decision == 2:
            crear_documento_comportamiento()
        if decision == 3:
            CrearFixture().run()
        if decision == 4:
            escribir()
        if decision == 5:
            creador = ExcelByArbol()
            creador.crear_arbol()

        return True

    def create_form_group_box(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        options = QComboBox()
        options.addItems([
            'crear documento',
            'crear documento comportamiento',
            'crear fixture',
            'escribir',
            'excel por arbol'
        ])
        options.currentIndexChanged.connect(self.at_select)
        layout.addRow(QLabel("Selecciona una opcion:"), options)
        self.formGroupBox.setLayout(layout)

    def at_select(self, i):
        self.decision = i + 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
