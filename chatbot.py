import speech_recognition as sr
import pyttsx3
import random
import wikipedia
import webbrowser

engine = pyttsx3.init()
r = sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)
greetings = ['hey there', 'hello', 'hi', 'hai', 'hey!', 'hey']
question = ['how are you', 'how are you doing', 'how you doing']
responses = ['Okay', "I'm fine"]
jokes = ["I just read that someone in London gets stabbed every 52 seconds. Poor guy."
"What's red and bad for your teeth? A brick."
"Why did Mozart kill all of his chickens? When he asked them who the best composer was, they all replied, 'Bach, Bach, Bach.'",
"Give a man a match, and he'll be warm for a few hours. Set a man on fire, and he will be warm for the rest of his life.",
"My wife and I have reached the difficult decision that we do not want children. If anybody does, please just send me your contact details and we can drop them off tomorrow.",
"Even people who are good for nothing have the capacity to bring a smile to your face. For instance, when you push them down the stairs.",
"I visited my friend at his new house. He told me to make myself at home. So I threw him out. I hate having visitors.",
"I was reading a great book about an immortal dog the other day. It was impossible to put down.",
"The other day, my wife asked me to pass her lipstick but I accidentally passed her a glue stick. She still isn't talking to me.",
"Never break someone's heart, they only have one. Break their bones instead, they have 206 of them.",
"I'll never forget my Granddad's last words to me just before he died. 'Are you still holding the ladder?'",
"It turns out a major new study recently found that humans eat more bananas than monkeys. It's true. I can't remember the last time I ate a monkey.",
"What's the difference between jelly and jam? You can't jelly a clown into the tiny car.",
"Why was the leper hockey game canceled? There was a face off in the corner.",
"Today was a terrible day. My ex got hit by a bus. And I lost my job as a bus driver!",
"'Just say NO to drugs!' Well, If I'm talking to my drugs, I probably already said yes.",
"I don't have a carbon footprint. I just drive everywhere.",
"It's important to have a good vocabulary. If I had known the difference between the words 'antidote' and 'anecdote,' one of my good friends would still be alive.",
"What's the last thing to go through a fly's head as it hits the windshield of a car going 70 mph? Its butt.",
"An apple a day keeps the doctor away. Or at least it does if you throw it hard enough.",
"Imagine if you walked into a bar and there was a long line of people waiting to take a swing at you. That's the punch line.",
"I have a fish that can breakdance! Only for 20 seconds though, and only once.",
"Today I decided to go visit my childhood home. I asked the residents if I could come inside because I was feeling nostalgic, but they refused and slammed the door on my face. My parents are the worst.",
"I have a joke about trickle down economics. But 99% of you will never get it."]
v1 = ['who made you', 'who created you']
v2 = ['who are you', 'what is your name', 'and your name']
v3 = ['abort', 'shut down', 'shutdown']
joke=['tell me a joke','make me laugh','hype me up with a joke']
while(1):
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio = r.listen(source)
            mytext = r.recognize_google(audio)
            mytext = mytext.lower()
            print(mytext)

            if mytext in greetings :
                choice = random.choice(greetings)
                print(choice)
                engine.say(choice)
                engine.runAndWait()

            elif mytext in question:
                choice2 = random.choice(responses)
                print(choice2)
                engine.say(choice2)
                engine.runAndWait()

            elif mytext in v1:
                print("Bharath is my Tony Stark. He designed me in half a day which he feels proud of.")
                engine.say("Bharath is my Tony Stark. He designed me in half a day which he feels proud of.")
                engine.runAndWait()

            elif mytext in v2:
                print("I am Donna, Bharath's assistant, just working for you for a few minutes")
                engine.say("I am Donna, Bharath's assistant, just working for you for a few minutes")
                engine.runAndWait()

            elif mytext in v3:
                print("Thank You and Have a Great Day!")
                engine.say("Thank You and Have a Great Day!")
                engine.runAndWait()
                exit()

            elif mytext in joke:
                choice3 = random.choice(jokes)
                print(choice3)
                engine.say(choice3)
                engine.runAndWait()

            elif mytext.split()[0] == 'search':
                mytext=mytext.split(' ',1)[1]
                engine.say("searching for "+ mytext + 'in google')
                engine.runAndWait()
                webbrowser.open_new_tab("www.google.com/search?q="+ mytext)

            elif mytext.split()[0] == 'play':
                mytext = mytext.split(' ',1)[1]
                engine.say("searching for "+ mytext + "in youtube")
                engine.runAndWait()
                webbrowser.open_new_tab("www.youtube.com/search?q="+ mytext)

            else:
                engine.say("Please wait, Let me check it on wikipedia")
                engine.runAndWait()
                print(wikipedia.summary(mytext))
                engine.say(wikipedia.summary(mytext))
                engine.runAndWait()

    except sr.RequestError as e:
        print("Could not recognize what you're saying: {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown")


            
