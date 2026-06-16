

# Gerenciador de Processos Linux 🐧⚙️

Um monitor e gerenciador de processos nativo para sistemas baseados em Linux, desenvolvido em Python e **PySide6**. O software atua diretamente sobre o sistema de arquivos virtual `/proc` do Kernel, oferecendo uma interface gráfica moderna com monitoramento em tempo real e controle operacional de tarefas correntes, utilizando conceitos avançados de multithreading.

*OBS.: Na aba **Releases** deste repositório, disponibilizamos o executável portátil para testes práticos.*

---

## 🎯 Objetivo do Projeto
O sistema tem como fito monitorar e manipular processos ativos no S.O. Linux, extraindo e estruturando de forma legível informações de baixo nível diretamente do Kernel:

* **PID:** Identificador único do processo.
* **User:** Usuário proprietário do processo.
* **Comando:** Nome do executável/tarefa.
* **Status:** Estado atual da thread (Executando, Dormindo, Zumbi, etc.) com estilização condicional.
* **Tempo de CPU:** Tempo total consumido em espaço de usuário e kernel.
* **NICE:** Índice de prioridade de agendamento de CPU.

---

## ✨ Funcionalidades Principais
* ⏸ **Pausar (`SIGSTOP`):** Congela temporariamente a execução de um processo.
* ▶ **Continuar (`SIGCONT`):** Retoma o processamento de uma tarefa pausada.
* ✕ **Finalizar (`SIGKILL`):** Encerra imediatamente a execução de um processo.
* 🔄 **Reiniciar:** Coleta o escopo do processo, finaliza o PID corrente e inicializa uma nova instância.
* ⚡ **Alterar Prioridade (NICE):** Altera a prioridade de agendamento (intervalo de -20 a 19).
* ▶ **Executar Novo Processo:** Abre e desacopla novos subprocessos via interface.
* 🔄 **Atualização Dinâmica:** Varredura em tempo real controlada via timers assíncronos.

---

## 📂 Estrutura do Projeto

```text
GERENCIADOR_PROCESSOS/
├── core/
│   ├── controller.py    # Regras de negócio e comunicação com Kernel
│   └── reader.py        # Parser e leitura de arquivos do /proc
├── interface/
│   ├── gui.py           # Janela Principal e componentes Qt
│   └── style.qss        # Customização visual (QSS)
├── utils/
│   └── formatters.py    # Auxiliares de formatação de dados
├── .gitignore           # Filtro de arquivos ignorados
├── main.py              # Ponto de entrada (Bootstrap)
├── main.spec            # Configuração do PyInstaller
├── README.md            # Documentação
└── requirements.txt     # Dependências (PySide6)

---

## 🚀 Como Executar e Integrar ao Sistema (Via AppImage)

Distribuímos o sistema pronto para uso no formato portátil **`.AppImage`**. O aplicativo conta com um sistema de **auto-integração**. Isso significa que, ao executá-lo pela primeira vez, ele se encarrega de se instalar sozinho na gaveta de aplicativos do seu Linux com o ícone oficial.

### Passo 1: Execução Inicial (Ativação)
1. Baixe o arquivo `Gerenciador_de_Processos-x86_64.AppImage` na aba de **Releases** do repositório.
2. Clique com o **botão direito do mouse** no arquivo baixado e selecione **Propriedades**.
3. Vá até a aba **Permissões** e ative a opção **"Permitir executar o arquivo como programa"** (ou ligue a chave correspondente à execução no seu sistema). Feche a janela.
4. Dê **dois cliques** para abrir o aplicativo pela primeira vez.

### Passo 2: Onde encontrar o aplicativo definitivo?
Assim que a interface gráfica do programa carregar, o sistema de auto-integração criará o atalho permanente no seu Linux. 

1. Você já pode fechar a janela do aplicativo.
2. Abra o **Menu/Painel de Aplicativos** do seu Linux (gaveta de aplicativos do Ubuntu/Debian/Mint) e pesquise por **"Gerenciador de Processos"**.
3. O aplicativo estará disponível nativamente, **com a imagem oficial do pinguim!**

> 💡 **Dica de Ouro:** A partir de agora, você não precisa mais clicar no arquivo `.AppImage` original que baixou. Se preferir, pode clicar com o botão direito no ícone do pinguim dentro do menu de aplicativos e selecionar **"Adicionar aos Favoritos"** ou **"Adicionar à Área de Trabalho"** para abrir o gerenciador com o visual perfeito direto da sua tela inicial!

---

## 💻 Execução Alternativa via Terminal

Se preferir rodar por linha de comando ou precisar depurar os logs de saída do Python, execute os comandos abaixo no diretório do arquivo baixado:

```bash
# Conceda a permissão de execução ao pacote
chmod +x Gerenciador_de_Processos-x86_64.AppImage

# Execute o programa diretamente
./Gerenciador_de_Processos-x86_64.AppImage
