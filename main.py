import sys
import os

# Garante que o Python encontre todas as pastas locais independentemente de onde ele for executado
caminho_raiz = os.path.dirname(os.path.abspath(__file__))
if caminho_raiz not in sys.path:
    sys.path.append(caminho_raiz)

from PySide6.QtWidgets import QApplication
from interface.gui import Interface

def main():
    app = QApplication(sys.argv)
    
    # Carrega o estilo QSS buscando o caminho correto a partir da raiz
    caminho_estilo = os.path.join(caminho_raiz, "interface", "style.qss")
    try:
        with open(caminho_estilo, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print(f"Aviso: Arquivo de estilo não encontrado em {caminho_estilo}")

    # Instancia e exibe a janela principal
    janela = Interface()
    janela.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()