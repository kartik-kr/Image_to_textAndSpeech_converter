from PIL import Image
import pytesseract
import pyttsx
text = pytesseract.image_to_string(Image.open('testimage.jpg'))
#print text from image
print (text)
engine = pyttsx.init()
#change voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 
#change the rate of speech
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.say(text)
engine.runAndWait()

