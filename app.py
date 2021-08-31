import speech_recognition as sr

re = sr.Recognizer()

file = open("speech_to_text.txt", "w")

with sr.Microphone() as source:

    print("Speak Something : ")
    audio = re.record(source, duration=10)

    try:

        text = re.recognize_google(audio)
        print('you said : {}'.format(text))
        file.write(text)
        file.close()

    except sr.UnknownValueError:

        print("Unknow Error Occurred")

    except sr.RequestError:

        print("Could not request results")
