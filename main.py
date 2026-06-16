import sys
import os

# Garante que o Python encontre todas as pastas locais independentemente de onde ele for executado
caminho_raiz = os.path.dirname(os.path.abspath(__file__))
if caminho_raiz not in sys.path:
    sys.path.append(caminho_raiz)

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from interface.gui import Interface

def main():
    app = QApplication(sys.argv)
    
    #PARA O LINUX: Define o nome interno do processo para o gerenciador de janelas
    app.setDesktopFileName("gerenciador_processos")

    # Define dinamicamente o caminho da pasta da interface (Desenvolvimento vs Executável)
    if getattr(sys, 'frozen', False):
        pasta_interface = os.path.join(sys._MEIPASS, "interface")
    else:
        pasta_interface = os.path.join(caminho_raiz, "interface")
        
    caminho_icone = os.path.normpath(os.path.join(pasta_interface, "icone.png"))
    icone_oficial = QIcon(caminho_icone)

    app.setWindowIcon(icone_oficial)
    
    # Carrega o estilo QSS buscando o caminho correto da pasta definida acima
    caminho_estilo = os.path.join(pasta_interface, "style.qss")
    try:
        with open(caminho_estilo, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print(f"Aviso: Arquivo de estilo não encontrado em {caminho_estilo}")

    # Instancia e exibe a janela principal
    janela = Interface()
    janela.setWindowIcon(icone_oficial) # Garante o ícone direto na barra de título da janela
    janela.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()