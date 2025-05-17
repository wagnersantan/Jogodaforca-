# 🎯 Jogo da Forca em Python

Este é um jogo clássico da **forca**, desenvolvido em Python para fins educacionais e de diversão. O jogador deve adivinhar uma palavra secreta, letra por letra, antes que o boneco seja "enforcado".

## 🧠 Como Funciona

- O programa sorteia uma palavra aleatória do arquivo `palavras.txt`.
- O jogador tenta adivinhar a palavra letra por letra.
- A cada erro, uma parte do boneco é desenhada.
- O jogo termina com vitória ao completar a palavra, ou derrota após 7 erros.

## 📁 Estrutura dos Arquivos

```text
.
├── forca.py          # Código principal do jogo
├── palavras.txt      # Lista de palavras usadas no jogo
└── README.md         # Este arquivo

## ▶️ Como Jogar

1. Clone o repositório ou copie os arquivos para sua máquina.
2. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
3. No terminal, execute:

```bash
python forca.py
## 🏆 Resultado

- **Vitória:** A palavra é completada sem 7 erros.
- **Derrota:** O boneco da forca é desenhado completo.

## 📌 Exemplo de Execução

*****************************************
****** Bem-vindo ao jogo da Forca *******
*****************************************
['_', '_', '_', '_', '_']
Qual letra? a
['_', 'A', '_', '_', 'A']
...
Parabéns, você ganhou!



