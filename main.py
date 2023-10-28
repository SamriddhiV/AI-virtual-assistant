import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init(driverName='sapi5')


def talk(text):
    machine.say(text)
    machine.runAndwait()


def input_instruction():
    try:
        with aa.Microphone(device_index=0) as origin:
            print('Listening..')
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "Jarvis" in instruction:
                instruction = instruction.replace('Jarvis', " ")
                print(instruction)
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


def play_Jarvis():
    talk("how can i assist you today?")
    while True:
        instruction = input_instruction()
        if instruction:
            if "play" in instruction:
                song = instruction.replace('play', "")
                talk("playing " + song)
                pywhatkit.playonyt(song)
            elif 'time' in instruction:
                time = datetime.datetime.now().strftime('%I:%M%p')
                talk('current time ' + time)

            elif 'date' in instruction:
                date = datetime.datetime.now().strftime('%d /%m /%Y ')
                talk("Today's date " + date)

            elif 'how are you' in instruction:
                talk('I m good')

            elif 'what is your name' in instruction:
                talk('my name is Jarvis')

            elif 'who is' in instruction:
                human = instruction.replace('who is', " ")
                info = wikipedia.summary(human, 1)
                print(info)
                talk(info)

            else:
                talk("Please repeat")



if __name__ == "__main__":
    play_Jarvis()
