import speech_recognition as sr
import pyttsx3 as ps
import google.generativeai as palm

engine = ps.init()
sr1 = sr.Recognizer()

class Voice_Assistant:
    
    def AI(x):
        palm.configure(api_key='')
        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        model = models[0].name

        completion = palm.generate_text(
                model = model,
                prompt = x,
                temperature = 1,
                max_output_tokens = 150,
                )

        Voice_Assistant.speak(completion.result)

    def speak(y):
        print(f'SyBot: {y}')
        engine.say(y)
        engine.runAndWait()

while True:
    with sr.Microphone() as source:
        print('Listening....')
        try:
            message = sr1.listen(source)
            response = sr1.recognize_google(message , language = 'en-in')

            if response.lower() in ['stop','bye','goodbye','close']:
                print('Ok then, Bye')
                engine.say('Ok then, bye')
                engine.runAndWait()
                break
    
            else:
                print(f'User: {response}')
                Voice_Assistant.AI(response)
                    
        except:
            print('Error, try again')
            engine.say('Error, try again')
            engine.runAndWait()
