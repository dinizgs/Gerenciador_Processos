*⚙️ Gerenciador de Processos Linux*

Um gerenciador de processos nativo para sistemas baseados em Linux desenvolvido em Python e PySide6. O software atua diretamente sobre o sistema de arquivos virtual `/proc` do Kernel, oferecendo uma interface gráfica moderna com monitoramento em tempo real e controle operacional de tarefas correntes.

*OBS.: Dentro do repositório presente, há o arquivo executável para testes práticos.*

---

## Objetivo do Projeto
O sistema tem como fito monitorar e manipular processos ativos no S.O. Linux, extraindo e estruturando de forma legível as seguintes informações de baixo nível:
* **PID:** Identificador único do processo.
* **User:** Usuário proprietário do processo.
* **Comando:** Nome do executável/tarefa.
* **Status:** Estado atual da thread (Executando, Dormindo, Zumbi, etc.) com estilização condicional.
* **Tempo de CPU:** Tempo total consumido em espaço de usuário e kernel traduzido em tempo real.
* **NICE:** Índice de prioridade de agendamento de CPU.

---

## Funcionalidades Principais
* ⏸ **Pausar (`SIGSTOP`):** Congela temporariamente a execução de um processo na RAM.
* ▶ **Continuar (`SIGCONT`):** Retoma o processamento de uma tarefa pausada.
* ✕ **Finalizar (`SIGKILL`):** Encerra imediatamente a execução de um processo.
* 🔄 **Reiniciar:** Coleta o escopo do processo, finaliza o PID corrente e inicializa uma nova instância.
* ⚡ **Alterar Prioridade (NICE):** Altera a prioridade de agendamento do processo entre os valores `-20` e `19`.
* ▶ **Executar Novo Processo:** Abre e desacopla novos subprocessos do sistema diretamente pela interface.
* 🔄 **Atualização Dinâmica:** Varredura em tempo real controlada via timers assíncronos protegidos contra quebra de seleção.

---

## Ferramentas Utilizadas
* **Ambiente de Desenvolvimento:** Python v3.12.3+
* **Interface Gráfica (GUI):** PySide6 v6.11.1+ (Engine Qt)
* **Estilização:** Custom QSS (Qt Style Sheets) & `QGraphicsDropShadowEffect` para efeitos neon dinâmicos.

---

## Modularização
```
GERENCIADOR_PROCESSOS/
├── core/
│   ├── __init__.py
│   ├── controller.py    # Regras de negócio e comunicação com Kernel (Sinais OS)
│   └── reader.py        # Parser e leitura de baixo nível dos arquivos do /proc
├── interface/
│   ├── __init__.py
│   ├── gui.py           # Janela Principal, Componentes Qt e Conexões de Slots/Signals
│   └── style.qss        # Customização visual da folha de estilos do sistema
├── utils/
│   ├── __init__.py
│   └── formatters.py    # Auxiliares de formatação de dados e strings
├── venv/                # Ambiente virtual isolado do Python
├── .gitignore
├── main.py              # Ponto de entrada (Bootstrap) da aplicação
├── README.md
└── requirements.txt     # Listagem de dependências do projeto
```
---

## Comandos para instalação dos Pacotes do PySide6 (linux):
- sudo apt update
- python3 -m venv venv
- source venv/bin/activate
- pip install pyside6