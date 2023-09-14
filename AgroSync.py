import openai
import pyttsx3
import speech_recognition as sr
import os
import datetime

# Configure a chave da API da OpenAI
api_key = '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'
openai.api_key = api_key

# Inicializar o engine de fala
engine = pyttsx3.init()

# Função para falar
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Função para interagir com a API GPT-3
def interagir_com_gpt3(pergunta):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente de agricultura."},
                {"role": "user", "content": pergunta},
            ]
        )
        resposta = response['choices'][0]['message']['content'].strip()
        return resposta
    except Exception as e:
        return str(e)

# Função para reconhecimento de voz
def reconhecer_fala():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        print("Diga o que precisa de cuidado...")
        audio = r.listen(source, timeout=5)

    try:
        pergunta = r.recognize_google(audio, language='pt-BR')
        print(f"Você: {pergunta}")
        return pergunta
    except sr.UnknownValueError:
        print("Desculpe, não entendi o que você disse.")
        return ""
    except sr.RequestError as e:
        print(f"Erro na requisição ao serviço de reconhecimento de voz: {e}")
        return ""

# Restante do código permanece o mesmo

# Informar a hora atual
hora_atual = datetime.datetime.now()
hora_formatada = hora_atual.strftime("%H:%M")
falar(f"Agora são {hora_formatada}")

# Informar as informações fictícias do clima
informacoes_clima = "A temperatura atual é 25°C e o tempo está ensolarado."
falar(informacoes_clima)

# Saudação inicial
falar("Como posso ajudar você hoje?")

# Loop principal
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Escolha uma opção ou faça uma pergunta:")
    print("1. Cuidados da Plantação")
    print("2. Leitura de Solo")
    print("3. Falar com Fornecedor de Fertilizantes")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada ou faça uma pergunta: ")

    if escolha == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        falar("Por favor, aguarde enquanto verifico os cuidados da plantação.")
        falar("Qual plantação você deseja saber mais? Por exemplo, 'cuidados com o milho'.")

        pergunta = reconhecer_fala()
        if pergunta:
            resposta_chatgpt = interagir_com_gpt3(pergunta)
            print("Assistente: " + resposta_chatgpt)
            falar(resposta_chatgpt)
            input("Pressione Enter para continuar...")
    elif escolha == "2":
        # Aqui você pode adicionar a funcionalidade de leitura de solo
        os.system('cls' if os.name == 'nt' else 'clear')
        falar("Por favor, aguarde enquanto realizo a leitura do solo.")
        # Adicione a lógica de leitura de solo aqui
        input("Pressione Enter para continuar...")
    elif escolha == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Aqui estão algumas marcas fictícias de fertilizantes para sua referência:")
        print("1. Fertilizante AgroMax - https://www.agromax-fertilizantes.com")
        print("2. Fertilizante GreenGrow - https://www.greengrow-fertilizantes.com")
        print("3. Fertilizante BioCrop - https://www.biocrop-fertilizantes.com")
        print("Espero que isso ajude!")
        input("Pressione Enter para continuar...")
    elif escolha == "4":
        print("Até logo!")
        break
    else:
        resposta_chatgpt = interagir_com_gpt3(escolha)
        print("Assistente: " + resposta_chatgpt)
        falar(resposta_chatgpt)
        input("Pressione Enter para continuar...")