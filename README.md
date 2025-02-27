# Jogo da Forca

Bem-vindo ao Jogo da Forca! Este é um jogo divertido e interativo onde você tenta adivinhar uma palavra secreta letra por letra. O jogo é feito em Python e utiliza um arquivo de texto para carregar as palavras.

## Funcionalidades

- Jogar a Forca com palavras aleatórias.
- Você pode inserir letras e terá um limite de tentativas.
- Mensagens de vitória e derrota são exibidas no final do jogo.

## Requisitos

- Python 3.x
- Um arquivo de texto chamado `palavras.txt` que contém as palavras que serão utilizadas no jogo. Cada palavra deve estar em uma linha separada.

## Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   cd seurepositorio

Crie o arquivo palavras.txt:

Crie um arquivo chamado palavras.txt na mesma pasta onde está o script forca.py. Adicione as palavras que você deseja usar no jogo, uma por linha.

Exemplo de conteúdo do palavras.txt:

python
programacao
forca
jogo

Execute o jogo:

Execute o script Python:

 
python forca.py
Jogue:

Siga as instruções na tela. Você será solicitado a adivinhar letras até que ganhe, perca ou esgote suas tentativas.

Estrutura do Código
O código é organizado em funções principais:

imprime_mensagem_abertura(): Exibe uma mensagem de boas-vindas.

carrega_palavra_secreta(): Carrega uma palavra aleatória do arquivo palavras.txt.

pede_chute(): Solicita ao jogador que forneça uma letra.

marca_chute_correto(): Atualiza a lista de letras acertadas se o chute estiver correto.

desenha_forca(): Exibe o desenho da forca baseado no número de erros.

jogar(): Função principal que controla o fluxo do jogo.

Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para fazer um fork do repositório e enviar um pull request.

Licença



