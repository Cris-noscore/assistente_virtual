# Importação das bibliotecas necessárias
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import pyjokes
import wikipediaapi
import webbrowser
from datetime import datetime
from pygame import mixer

# Função para capturar áudio do microfone
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)  # Ajusta o nível de ruído
        print("Estou ouvindo...")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print("Você disse:", said)
        except sr.UnknownValueError:
            speak("Desculpe, não entendi.")
        except sr.RequestError:
            speak("Erro na conexão com o serviço de reconhecimento.")
    return said.lower()

# Função para converter texto em fala
def speak(text):
    tts = gTTS(text=text, lang='pt')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

# Função para pesquisar na Wikipedia
def search_wikipedia(query):
    wiki = wikipediaapi.Wikipedia(
    language='pt',
    user_agent='assistente_virtual'
)
    page = wiki.page(query)

    if page.exists():
        return page.summary[:500]  # Retorna os primeiros 500 caracteres do resumo
    else:
        return "Não encontrei nada sobre isso na Wikipedia."

# Função para responder comandos
def respond(text):
    print("Comando recebido:", text)

    if 'youtube' in text:
        speak("O que deseja buscar no YouTube?")
        keyword = get_audio()
        if keyword:
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.open(url)
            speak(f"Aqui estão os resultados para {keyword} no YouTube.")

    elif 'pesquisar' in text or 'wikipedia' in text:
        speak("O que deseja pesquisar na Wikipedia?")
        query = get_audio()
        if query:
            result = search_wikipedia(query)
            speak("De acordo com a Wikipedia:")
            print(result)
            speak(result)

    elif 'piada' in text:
        joke = pyjokes.get_joke(language="en")
        print(joke)
        speak(joke)

    elif 'horas' in text:
        strTime = datetime.now().strftime("%H:%M")
        print(strTime)
        speak(f"Agora são {strTime} horas.")

    elif 'tocar música' in text:
        speak("Tocando música...")
        music_dir = "C:\\Users\\SeuUsuario\\Músicas\\"  # Ajuste para o diretório correto
        songs = os.listdir(music_dir)
        if songs:
            playmusic(os.path.join(music_dir, songs[0]))
        else:
            speak("Não encontrei músicas na pasta.")

    elif 'parar música' in text:
        speak("Parando música.")
        stopmusic()

    elif 'sair' in text or 'fechar' in text:
        speak("Até mais!")
        exit()

# Função para tocar música
def playmusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()

# Função para parar música
def stopmusic():
    mixer.music.stop()

# Loop principal do assistente
while True:
    comando = get_audio()
    respond(comando)