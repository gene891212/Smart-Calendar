import speech_recognition
import pyaudio


def get_speech_text():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("請開始說話:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="zh-TW")
    except r.UnknowValueError:
        text = "無法翻譯"
    except sr.RequestError as e:
        text = "無法翻譯{0}".format(e)
    return text

if __name__ == "__main__":
    text = get_speech_text()
    print(text)
