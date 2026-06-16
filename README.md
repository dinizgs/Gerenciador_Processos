# Gerenciador de Processos Linux 🐧⚙️

Um monitor e gerenciador de processos nativo para sistemas baseados em Linux, desenvolvido em Python e **PySide6**. O software atua diretamente sobre o sistema de arquivos virtual `/proc` do Kernel, oferecendo uma interface gráfica moderna com monitoramento em tempo real e controle operacional de tarefas correntes, utilizando conceitos avançados de multithreading.

*OBS.: Na aba **Releases** deste repositório, disponibilizamos o executável portátil para testes práticos.*

---

## 🎯 Objetivo do Projeto
O sistema tem como objetivo monitorar e manipular processos ativos no S.O. Linux, extraindo e estruturando de forma legível informações de baixo nível diretamente do Kernel:

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


```

## 🛠️ Ambiente de Desenvolvimento Local
Para clonar e executar o código fonte diretamente para fins de manutenção ou estudo:

1. Configuração do Ambiente
Abra o seu terminal na pasta raiz do projeto e execute:

```bash
# Atualize os pacotes e crie o ambiente virtual
sudo apt update
python3 -m venv venv

# Ative o ambiente virtual
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

```
2. Execução
Com o ambiente ativado, rode:

```bash
python main.py
```
💡 Solução de Problemas
Se o programa não abrir (comum em distros muito recentes sem suporte FUSE 2), instale a biblioteca necessária:

```bash
sudo apt install libfuse2 -y
```

## 🚀 Como Executar e Integrar ao Sistema (Linux)

Distribuímos o sistema no formato portátil **`.AppImage`**. O aplicativo conta com um sistema de **auto-integração**. Isso significa que ao executá-lo pela primeira vez, ele se instala automaticamente no menu do seu sistema com o ícone oficial.

Siga os passos abaixo:

### Passo 1: Execução Inicial (Ativação)
1. Baixe o arquivo `Gerenciador_de_Processos-x86_64.AppImage` na aba de Releases.
2. Clique com o **botão direito do mouse** no arquivo baixado e selecione **Propriedades**.
3. Vá até a aba **Permissões** e ative a opção **"Permitir executar o arquivo como programa"** (ou ligue a chave correspondente). Feche a janela.
4. Dê **dois cliques** para abrir o aplicativo pela primeira vez.

---

### Passo 2: Onde encontrar o aplicativo definitivo?
Assim que o programa abrir, o sistema de auto-integração criará o atalho definitivo no seu Linux. 

1. Você já pode fechar o aplicativo.
2. Abra o **Menu/Painel de Aplicativos** do seu Linux (gaveta de aplicativos do Ubuntu/Debian) e pesquise por **"Gerenciador de Processos"**.
3. O aplicativo estará lá disponível nativamente, **com a imagem oficial do pinguim!**

> 💡 **Dica:** A partir de agora, você não precisa mais clicar no arquivo `.AppImage` que baixou. Se quiser, pode clicar com o botão direito no ícone do pinguim dentro do menu e selecionar **"Adicionar aos Favoritos"** ou **"Adicionar à Área de Trabalho"** para abrir o gerenciador direto da sua tela inicial com o visual perfeito!

---

## 💻 Execução via Terminal

Se preferir rodar por linha de comando ou precisar depurar a saída no terminal, execute:

```bash
# Concede a permissão de execução
chmod +x Gerenciador_de_Processos-x86_64.AppImage

# Execute o programa
./Gerenciador_de_Processos-x86_64.AppImage
