from email.mime import audio
import speech_recognition as sr

import os

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:

        #Chama um algoritimo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        #Frase para usuário dizer algo
        print("Diga alguma coisa: ")

        #Armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:

        #Passa a variável para o algoritimo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language= 'pt-BR')

        if "navegador" in frase:
            os.system("start Chrome.exe")
        
        elif "Excel" in frase:
            os.system("start Excel.exe")

        #Retorna a frase pronunciada
        print("Você disse: " + frase)

    #Se não reconheceu o padrão de fala, exibe a mensagem
    except sr.UnknownValueError:
        print("Não entendi")

    return frase

ouvir_microfone()