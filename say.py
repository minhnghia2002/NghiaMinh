import pyttsx3
say = pyttsx3.init()
while True:
	you = input()
	if you == "hello":
		print("Computer: Hello Minh Nghia")
		say.say("Hello Minh Nghia")
	elif "hm" in you:
		print("What are you doing")
		say.say("What are you doing?")
	elif "miss hien" in you:
		print("Does she miss you too?")
		say.say("Does she miss you too")
	elif "i think no" in you:
		print("This is sad story")
		say.say("This is sad story")
	elif "i know" in you:
		print("You need going to sleep now baby")
		say.say("You need going to sleep now baby")
	elif "ok" in you:
		print("Good night Minh Nghia")
		say.say("Good night Minh Nghia")
	elif "bye" in you:
		break
	else:
		print("Say something")
		say.say("Say something")
	say.runAndWait()