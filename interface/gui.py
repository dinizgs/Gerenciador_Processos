import sys
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit, QLabel, QDialog, QSpinBox, QMessageBox, QDialogButtonBox,
    QFormLayout, QTextEdit, QStatusBar, QApplication
)

class Interface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gerenciador Processos Linux" )




if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec())

    

