import speech_recognition as sr
import pyttsx3 as ps
import google.generativeai as palm

class Voice_Assistant:
    def mic():
        sr1 = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening....')
            message = sr1.listen(source)
            response = sr1.recognize_google(message , language = 'en-in')
            print(response)

            Voice_Assistant.AI(response)

    def AI(x):
        palm.configure(api_key='AIzaSyB9sslPFgMyFQaXMCB7y-jaXauDNM-NHG8')
        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        model = models[0].name

        completion = palm.generate_text(
                model = model,
                prompt = x,
                temperature = 1,
                max_output_tokens = 150,
                )

        Voice_Assistant.speak(completion)

    def speak(y):
        print(y.result)
        engine = ps.init()
        engine.say(y.result)
        engine.runAndWait()

while True:
    Voice_Assistant.mic()
