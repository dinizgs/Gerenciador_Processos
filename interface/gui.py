import sys
import os
caminho = os.path.dirname(os.path.abspath(__file__))

raiz_projeto = os.path.dirname(caminho)

if raiz_projeto not in sys.path:
    sys.path.append(raiz_projeto)

from core import controller,reader
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
        titulo.setObjectName("titulo_gerenciador")
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
        cabecalho.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        cabecalho.setSectionResizeMode(2, regra_esticar)

        # Seleção de linhas por processo
        self.tabela_itens.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabela_itens.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        layout_inferior = QHBoxLayout()
        layout_inferior.addStretch()

        #---------Executar um novo processo----------
        #---------Parte da Esquerda------------------
        label_novo_processo = QLabel("Novo Processo:")
        self.texto_comando = QLineEdit()
        self.texto_comando.setPlaceholderText("Digite um comando...")
        self.texto_comando.setMaximumWidth(300)

        button_executar_comando = QPushButton("▶ Executar")

        layout_inferior.addWidget(label_novo_processo)
        layout_inferior.addWidget(self.texto_comando)
        layout_inferior.addWidget(button_executar_comando)
        
        #Adicionar um espaçamento entre a parte da direita e esquerda
        layout_inferior.setSpacing(60)
        label_separar_visual = QLabel("||")
        layout_inferior.addWidget(label_separar_visual)

        #-----------Alterar a prioridade de um processo(NICE)----------
        #-----------Parte da Direita-----------------------------------
        label_alterar_prioridade = QLabel("Alterar Prioridade(NICE):")
        self.spin_box_nice = QSpinBox()
        self.spin_box_nice.setRange(-20,19)
        self.spin_box_nice.setValue(0)

        button_aplicar_nice = QPushButton("⚡ Aplicar")

        layout_inferior.addWidget(label_alterar_prioridade)
        layout_inferior.addWidget(self.spin_box_nice)
        layout_inferior.addWidget(button_aplicar_nice)

        layout_inferior.addStretch()

        #Adicionando ao layout principal
        layout_principal.addLayout(layout_inferior)


        #Atualização da tabela a cada 3 segundos, para não travar
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_tabela)
        self.timer.start(3000)
        self.atualizar_tabela()

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
        lista_processos = reader.listagem_dados_processos()

        self.tabela_itens.setRowCount(0)

        for processo in lista_processos:
            linha_atual = self.tabela_itens.rowCount()
            self.tabela_itens.insertRow(linha_atual)

            item_pid = QTableWidgetItem(str(processo["Pid"]))
            item_user = QTableWidgetItem(str(processo["User"]))
            item_comando = QTableWidgetItem(str(processo["Comando"]))
            item_status = QTableWidgetItem(str(processo["Status"]))
            item_time = QTableWidgetItem(str(processo["Time"]))
            item_nice = QTableWidgetItem(str(processo["Nice"]))

            self.tabela_itens.setItem(linha_atual,0,item_pid)
            self.tabela_itens.setItem(linha_atual,1,item_user)
            self.tabela_itens.setItem(linha_atual,2,item_comando)
            self.tabela_itens.setItem(linha_atual,3,item_status)
            self.tabela_itens.setItem(linha_atual,4,item_time)
            self.tabela_itens.setItem(linha_atual,5,item_nice)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Descobre o caminho exato da pasta onde este arquivo gui.py está salvo
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Aponta para o arquivo correto: "stylesheet.qss" dentro da pasta da interface
    caminho_estilo = os.path.join(diretorio_atual, "style.qss")

    try:
        with open(caminho_estilo, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())

    except FileNotFoundError:
        # Se o arquivo sumir, o app abre sem estilo, mas não crasha a execução
        print(f"Aviso: O arquivo de estilos não foi encontrado em: {caminho_estilo}")

    except Exception as e:
        print(f"Erro ao carregar o QSS: {e}")

    janela = Interface()
    janela.show()
    sys.exit(app.exec())