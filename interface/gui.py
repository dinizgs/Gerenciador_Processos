import sys
import os
caminho = os.path.dirname(os.path.abspath(__file__))

raiz_projeto = os.path.dirname(caminho)

if raiz_projeto not in sys.path:
    sys.path.append(raiz_projeto)

from core import controller
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit, QLabel, QDialog, QSpinBox, QMessageBox, QDialogButtonBox,
    QFormLayout, QTextEdit, QStatusBar, QApplication, QHeaderView
)
from PySide6.QtCore import QTimer, Qt

class Interface(QMainWindow):
    def __init__(self):
        super().__init__()

        # Criação da base:
        self.setWindowTitle("Gerenciador Processos Linux")

        janela_central = QWidget()
        self.setCentralWidget(janela_central)

        layout_principal = QVBoxLayout()
        janela_central.setLayout(layout_principal)
        
        # -------------------------------------------------------------------
        # Layout do topo (Botões de controle rápido)
        
        self.layout_topo_botoes = QHBoxLayout()
        button_pausar = QPushButton("⏸ Pausar")
        button_continuar = QPushButton("▶ Continuar")
        button_finalizar = QPushButton("✕ Finalizar")
        button_reiniciar = QPushButton("🔄 Reiniciar")
        button_atualizar = QPushButton("🔄 Atualizar")

        self.layout_topo_botoes.addWidget(button_pausar)
        self.layout_topo_botoes.addWidget(button_continuar)
        self.layout_topo_botoes.addWidget(button_finalizar)
        self.layout_topo_botoes.addWidget(button_reiniciar)

        button_pausar.clicked.connect(self.pausar_processo_gui)
        button_continuar.clicked.connect(self.continuar_processo_gui)
        button_finalizar.clicked.connect(self.finalizar_processo_gui)
        button_reiniciar.clicked.connect(self.reiniciar_processo_gui)

        #Empurra o próximo botão para o canto direito
        self.layout_topo_botoes.addStretch()

        # Adiciona o botão isolado na direita
        self.layout_topo_botoes.addWidget(button_atualizar)
        button_atualizar.clicked.connect(self.atualizar_tabela)

        # Entrega a barra de botões primeiro para o layout principal (Fica no topo!)
        layout_principal.addLayout(self.layout_topo_botoes)

        # -------------------------------------------------------------------
        #Título (Logo abaixo dos botões)
        
        titulo = QLabel("⚙️Gerenciador de Processos no Linux")
        layout_principal.addWidget(titulo)

        # -------------------------------------------------------------------
        #Tabela (Por último, ocupando o centro da tela)
        
        self.tabela_itens = QTableWidget()
        self.tabela_itens.setColumnCount(6)
        titulo_colunas = ["PID", "User", "Comando", "Status", "Tempo de CPU", "NICE"]
        self.tabela_itens.setHorizontalHeaderLabels(titulo_colunas)
        
        # Entrega a tabela para o layout principal
        layout_principal.addWidget(self.tabela_itens)

        # Regra para expandir a coluna do Comando
        regra_esticar = QHeaderView.ResizeMode.Stretch
        cabecalho = self.tabela_itens.horizontalHeader()
        cabecalho.setSectionResizeMode(2, regra_esticar)

        # Seleção de linhas por processo
        self.tabela_itens.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabela_itens.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

    def pausar_processo_gui(self):
        linha_selecionada = self.tabela_itens.currentRow() 
        if linha_selecionada == -1: #Essa condicional filtra o caso de não ter processos selecionados.
            QMessageBox.warning(self, "Warning", "Algum processo deve ser selecionado!")
            return

        #Como o PID é a primeira linha dentre as 6, seria o índice 0, ou coluna 0.
        pid = self.tabela_itens.item(linha_selecionada, 0).text()
        conclusao = controller.bloquear_processo(pid)

        if conclusao:
            QMessageBox.information(self, "Ação concluída!", f"{pid} bloqueado")
        else:
            QMessageBox.critical(self, "Erro!", f"Ação não concluída.")

    def continuar_processo_gui(self):
        linha_selecionada = self.tabela_itens.currentRow() 
        if linha_selecionada == -1: #Essa condicional filtra o caso de não ter processos selecionados.
            QMessageBox.warning(self, "Warning", "Algum processo deve ser selecionado!")
            return

        pid = self.tabela_itens.item(linha_selecionada, 0).text()
        conclusao = controller.continuar_processo(pid)

        if conclusao:
            QMessageBox.information(self, "Ação concluída!", f"{pid} continua em execução")
        else:
            QMessageBox.critical(self, "Erro!", f"Ação não concluída.")

    def finalizar_processo_gui(self):
        linha_selecionada = self.tabela_itens.currentRow()
        if linha_selecionada == -1: #Essa condicional filtra o caso de não ter processos selecionados.
            QMessageBox.warning(self, "Warning", "Algum processo deve ser selecionado!")
            return

        pid = self.tabela_itens.item(linha_selecionada, 0).text()
        conclusao = controller.finalizar_processo(pid)
        
        if conclusao:
            QMessageBox.information(self, "Ação concluída!", f"{pid} finalizado!")
        else:
            QMessageBox.critical(self, "Erro!", f"Ação não concluída.")

    def reiniciar_processo_gui(self):
        linha_selecionada = self.tabela_itens.currentRow()
        if linha_selecionada == -1: #Essa condicional filtra o caso de não ter processos selecionados.
            QMessageBox.warning(self, "Warning", "Algum processo deve ser selecionado!")
            return

        pid = self.tabela_itens.item(linha_selecionada, 0).text()
        conclusao = controller.reiniciar_processo(pid)
        
        if conclusao:
            QMessageBox.information(self, "Ação concluída!", f"{pid} reiniciado!")
        else:
            QMessageBox.critical(self, "Erro!", f"Ação não concluída.")

    def atualizar_tabela(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec())