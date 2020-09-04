import pyttsx3
import speech_recognition as sr

def takeInput():
	r = sr.Recognizer()
	dictionary= {
		"single": 1,
		"double": 2,
		"triple": 3,
		"quadruple": 4,
		"quintuple": 5,
		"sextuple": 6,
		"septuple": 7,
		"octuple": 8,
		"nonuple": 9,
		"decuple": 10
	}
	with sr.Microphone() as source:
		print("Listening")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("recognizing...")
		query = str(r.recognize_google(audio, language='en-in'))
		print(query)
		word = query.split(" ")
		if word[0] in dictionary.keys():
			text = ''
			for w in word[1:]:
				text+=w
			print((dictionary[word[0]]*text).upper())
	except Exception as e:
		print("Speak again")


if _name_ == '_main_':
	takeInput()
