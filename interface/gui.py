import sys
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit, QLabel, QDialog, QSpinBox, QMessageBox, QDialogButtonBox,
    QFormLayout, QTextEdit, QStatusBar, QApplication, QHeaderView
)

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
        
        #Empurra o próximo botão para o canto direito
        self.layout_topo_botoes.addStretch()

        # Adiciona o botão isolado na direita
        self.layout_topo_botoes.addWidget(button_atualizar)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Interface()
    janela.show()
    sys.exit(app.exec())