

# Gerenciador de Processos Nativos 🐧⚙️

Um monitor e gerenciador de processos leve e intuitivo, desenvolvido em Python utilizando **PySide6** para a interface gráfica e conceitos avançados de programação concorrente (multithreading).

---

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
# Conceda a permissão de execução
chmod +x Gerenciador_de_Processos-x86_64.AppImage

# Execute o programa
./Gerenciador_de_Processos-x86_64.AppImage
