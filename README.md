# Assistente Virtual em Python

Este projeto é um Assistente Virtual desenvolvido em Python, que utiliza reconhecimento de fala, conversão de texto em fala e consultas à Wikipedia. O objetivo é fornecer uma aplicação interativa que responda a comandos de voz, como buscar informações na Wikipedia, tocar música, contar piadas e fornecer a hora atual.

## Funcionalidades

- **Reconhecimento de Fala:** Captura comandos de voz do usuário usando a biblioteca `SpeechRecognition`.
- **Conversão de Texto em Fala:** Utiliza a biblioteca `gTTS` para converter texto em áudio e reproduzir a resposta.
- **Pesquisa na Wikipedia:** Realiza buscas e retorna resumos de artigos da Wikipedia utilizando a biblioteca `wikipediaapi`.
- **Integração com YouTube:** Permite pesquisas de vídeos diretamente no YouTube.
- **Contador de Piadas:** Gera piadas aleatórias usando a biblioteca `pyjokes`.
- **Música:** Toca músicas de uma pasta específica no sistema.
- **Informação de Hora:** Retorna a hora atual ao usuário.

## Requisitos

Para executar o projeto, você precisará das seguintes bibliotecas Python:

- `speech_recognition`
- `gtts`
- `playsound`
- `pyjokes`
- `wikipediaapi`
- `webbrowser`
- `pygame`

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

bash

pip install SpeechRecognition gtts playsound pyjokes wikipedia-api pygame

Como Usar

Clone o repositório para a sua máquina local:

bash

git clone https://github.com/Cris-noscore/assistente_virtual.git

Navegue até o diretório do projeto:

bash

cd assistente_virtual

Instale as dependências necessárias se ainda não o fez.

Execute o script Python:

bash

python assistente_virtual.py

Interaja com o assistente virtual ao seguir as instruções de voz.
