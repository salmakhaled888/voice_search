import speech_recognition as sr
from bidi.algorithm import get_display
import arabic_reshaper

r = sr.Recognizer()

with sr.Microphone() as src:
    print('Say something...')
    r.adjust_for_ambient_noise(src, duration=1)  # Adjust for noise
    audio = r.listen(src)
    
try:
    # Recognize speech and handle Arabic text appropriately
    recognized_text = r.recognize_google(audio, language='ar-AR',show_all = True)
    recognized_text = recognized_text['alternative'][0].get('transcript')
    reshaped_text = arabic_reshaper.reshape(recognized_text)  # Reshape Arabic letters
    bidi_text = get_display(reshaped_text)  # Apply BiDi formatting
    print(bidi_text.lower())  # Convert to lowercase for consistency

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
