# Gerenciador de Processos Nativos 🐧⚙️

Um monitor e gerenciador de processos leve e intuitivo, desenvolvido em Python utilizando **PySide6** para a interface gráfica e conceitos avançados de programação concorrente (multithreading).

---

## 🚀 Como Executar o Aplicativo (Linux)

Distribuímos o sistema no formato portátil **`.AppImage`**. Isso significa que você não precisa instalar nada no seu sistema: basta baixar o arquivo único e executá-lo.

Abaixo estão as duas maneiras simples de rodar o gerenciador:

### Opção 1: Pela Interface Gráfica (Recomendado)

Para abrir o programa dando apenas dois cliques na sua Área de Trabalho ou pasta de Downloads, siga estes passos:

1. Clique com o **botão direito do mouse** em cima do arquivo `.AppImage` baixado e selecione **Propriedades**.
2. Vá até a aba **Permissões** e ative a opção **"Permitir executar o arquivo como programa"** (ou ligue a chave correspondente). Feche a janela.
3. Se o arquivo estiver na Área de Trabalho (Ubuntu/GNOME), clique com o **botão direito** nele mais uma vez e selecione **"Permitir Lançamento"** (*Allow Launching*). Isso fará o ícone do sistema aparecer automaticamente.
4. Agora é só dar **dois cliques** ou selecionar **"Executar como um programa"** ao clicar com o botão direito!

---

### Opção 2: Pelo Terminal

Se preferir rodar por linha de comando ou precisar depurar a saída no terminal, execute:

```bash
# 1. Entre na pasta onde salvou o arquivo
cd ~/Downloads

# 2. Conceda a permissão de execução
chmod +x Gerenciador_de_Processos-x86_64.AppImage

# 3. Execute o programa
./Gerenciador_de_Processos-x86_64.AppImage
