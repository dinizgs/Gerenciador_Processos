import sys
import os

# Garante que o Python encontre todas as pastas locais independentemente de onde ele for executado
caminho_raiz = os.path.dirname(os.path.abspath(__file__))
if caminho_raiz not in sys.path:
    sys.path.append(caminho_raiz)

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from interface.gui import Interface

def integrar_sistema(pasta_interface):
    # Só executa se estiver no Linux e rodando de dentro do AppImage empacotado
    if sys.platform.startswith('linux') and 'APPIMAGE' in os.environ:
        import shutil
        
        pasta_atalhos = os.path.expanduser("~/.local/share/applications")
        pasta_icones = os.path.expanduser("~/.local/share/icons")
        
        caminho_atalho = os.path.join(pasta_atalhos, "gerenciador_processos.desktop")
        caminho_icone_sistema = os.path.join(pasta_icones, "gerenciador_processos.png")
        
        # Garante que as pastas ocultas de integração do usuário existam
        os.makedirs(pasta_atalhos, exist_ok=True)
        os.makedirs(pasta_icones, exist_ok=True)
        
        # 1. Copia o ícone para a pasta de ícones do sistema do usuário
        caminho_icone_origem = os.path.normpath(os.path.join(pasta_interface, "icone.png"))
        if os.path.exists(caminho_icone_origem) and not os.path.exists(caminho_icone_sistema):
            shutil.copy(caminho_icone_origem, caminho_icone_sistema)
            
        # 2. Cria o arquivo de atalho .desktop apontando para o AppImage atual
        if not os.path.exists(caminho_atalho):
            caminho_appimage = os.environ.get('APPIMAGE')
            
            conteudo_desktop = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=Gerenciador de Processos
Comment=Monitor de Processos nativo em Python e PySide6
Exec={caminho_appimage}
Icon=gerenciador_processos
Terminal=false
Categories=System;Utility;
"""
            with open(caminho_atalho, "w", encoding="utf-8") as f:
                f.write(conteudo_desktop)
            
            # Dá permissão de execução para o arquivo .desktop criado
            os.chmod(caminho_atalho, 0o755)

def main():
    app = QApplication(sys.argv)
    
    # PARA O LINUX: Define o nome interno do processo para o gerenciador de janelas
    app.setDesktopFileName("gerenciador_processos")

    # Define dinamicamente o caminho da pasta da interface (Desenvolvimento vs Executável)
    if getattr(sys, 'frozen', False):
        pasta_interface = os.path.join(sys._MEIPASS, "interface")
    else:
        pasta_interface = os.path.join(caminho_raiz, "interface")
        
    # CHAMA A FUNÇÃO DE INTEGRAÇÃO PASSANDO A PASTA DA INTERFACE CORRETA
    integrar_sistema(pasta_interface)
        
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