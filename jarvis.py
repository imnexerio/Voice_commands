import sys
import face_recognition
import cv2
import numpy as np
import pickle

video_capture = cv2.VideoCapture(1)

all_face_encodings = {'santosh': ([-0.08620673,  0.0687653 , -0.00608819, -0.03519192, -0.09629069,
    0.02071193,  0.00855641, -0.0746007 ,  0.20025523, -0.19063942,
    0.23173384, -0.01975415, -0.19306482, -0.09184648, -0.02485181,
    0.12691274, -0.13205203, -0.23288512, -0.08447211, -0.04476186,
    0.0083975 , -0.0296244 , -0.0538367 ,  0.0996822 , -0.11422063,
    -0.39109814, -0.03008146, -0.08237354,  0.00964145, -0.10379514,
    0.01887341,  0.08326089, -0.2100599 , -0.04585231, -0.03458627,
    0.15673032, -0.04124431,  0.02592537,  0.22747248,  0.03232506,
    -0.23795892,  0.04985239, -0.0171667 ,  0.3682757 ,  0.11798345,
    0.05134935,  0.01320769, -0.0422096 ,  0.09669503, -0.21262598,
    0.07605252,  0.16217186,  0.11024585,  0.02930695, -0.01529235,
    -0.11060968, -0.05178311,  0.09883492, -0.19042166,  0.05386725,
    0.05107993, -0.08046649, -0.07053865, -0.08853689,  0.28919473,
    0.1427469 , -0.11267848, -0.14243214,  0.19903164, -0.20890479,
    -0.08105254,  0.07197691, -0.09797259, -0.14822087, -0.2282711 ,
    0.0713177 ,  0.44073999,  0.10898171, -0.16698462,  0.0021062 ,
    -0.05878554, -0.02249282,  0.10918788,  0.13914604, -0.01934218,
    0.0422359 , -0.05627656,  0.0509939 ,  0.21402936,  0.04171608,
    -0.08584393,  0.17579725,  0.03536662,  0.00843763,  0.05709684,
    -0.01475102, -0.03864821,  0.01387846, -0.18548468, -0.02710009,
    0.00405915, -0.01406179, -0.01352922,  0.06071987, -0.11533216,
    0.17780612,  0.00737498,  0.02268635,  0.05493347,  0.11715318,
    -0.12227686, -0.13134263,  0.15357852, -0.25482872,  0.18621401,
    0.14612481,  0.06547383,  0.13273469,  0.09938824,  0.08322583,
    0.02706247, -0.0312997 , -0.23157075, -0.05897343,  0.0765569 ,
    -0.02074298,  0.11898391,  0.00958223])}

known_face_encodings = list(all_face_encodings.values())

known_face_names = list (all_face_encodings.keys())

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

name = ''

while name == '':

    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "sir"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break


video_capture.release()
cv2.destroyAllWindows()
try:
    
    import pyttsx3,webbrowser,smtplib,random,wikipedia,datetime,wolframalpha,os,sys,feedparser,pyjokes
    import speech_recognition as sr

    engine = pyttsx3.init('sapi5')

    client = wolframalpha.Client('your wloframalpha api id')

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[len(voices)-1].id)

    def speak(audio):
        print('Jarvis : ' + audio)
        engine.say(audio)
        engine.runAndWait()

    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            speak('Good Morning! '+name)

        if currentH >= 12 and currentH < 18:
            speak('Good Afternoon! '+name)

        if currentH >= 18 and currentH !=0:
            speak('Good Evening! '+name)

    greetMe()

    if name=='santosh':
        username = 'santosh52628@gmail.com'
        password = 'qwertytrewrrtewq'
        speak('Please choose a way to interact')

    else:

        username = str(input("Enter your username : "))
        password = str(input("Enter your password : "))

        if username == '' or username == 'default':
            username ='skp09876789@gmail.com'
        if password == '' or password == 'default':
            password ='hello everyone'



        speak('Hello sir , I am your digital assistant!!!!')
        speak('How may I help you?')
        speak('I can help you in two ways : ')
        speak('1 - Through voice command!')
        speak('2 - Through typing')
        speak('To enable voice command say  : activate voice command')
        speak('To enable typing say  : activate typing')
        speak('I am developed by  the Santosh ')

    re = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        re.pause_threshold =  1
        audio = re.listen(source)
    try:
        queryte = re.recognize_google(audio, language='en-in')
        print('User: ' + queryte + '\n')

    except :
        speak('sorry sir! due to some error by default typing mode is activated ')
        queryte='text mode'


    if queryte =='1' or queryte == 'voice' or queryte == 'voice command' or queryte == 'activate voice command' or queryte == 'activate voice mode' :
        speak('sir you have choosen voice mode')
        def myCommand():
                r = sr.Recognizer()                                                                                   
                with sr.Microphone() as source:                                                                       
                    print("Listening...")
                    r.pause_threshold =  1
                    audio = r.listen(source)
                try:
                    query_ask = r.recognize_google(audio, language='en-in')
                    print('User: ' + query_ask + '\n')
                    return query_ask
                except sr.UnknownValueError:
                    plzMsgs = ['Sorry sir! I didn\'t get that! Try typing the command!!','sorry sir i am unable to recognise your voice kindly try typing the command','sir plz type the command']
                    speak(random.choice(plzMsgs))
                    query_ask = str(input('Command: '))
                    print('User: ' + query_ask + '\n')
                    return query_ask
                except  sr.RequestError:
                    onMsgs = ['sorry sir! i am not online now','sorry sir! i am unable to talk to the internet','sorry sir i and internet are\'t talking now',]
                    speak(random.choice(onMsgs))
                    sys.exit()

    else:
        speak('sir you have choosen text mode')
        def myCommand():
            query_ask = str(input('Command: '))
            return query_ask


    def news():
        def parseRSS( rss_url ):
            return feedparser.parse( rss_url )
        
        def getHeadlines(rss_url):
            headlines = []
        
            feed = parseRSS(rss_url)
            for newsitem in feed['items']:
                headlines.append(newsitem['title'])
        
            return headlines
        
        allheadlines = []
        
        newsurls = {'googlenews': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',}
        
        for key, url in newsurls.items():
            
            allheadlines.extend(getHeadlines(url))
        
        
        for hl in allheadlines:
            newstell=hl
            speak(newstell)


    if __name__ == '__main__':

        while True:
        
            query_ask = myCommand()
            query_ask = query_ask.lower()
            
            if query_ask == 'open youtube' or query_ask == 'youtube' or query_ask == 'www.youtube.com' or query_ask == 'youtube.com' :
                stMsgs = ['opening youtube','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                webbrowser.open('www.youtube.com')

            elif query_ask == 'open google' or query_ask == 'google' or query_ask == 'www.google.com' or query_ask == 'google.com' :
                stMsgs = ['opening google','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                webbrowser.open('www.google.com')

            elif query_ask == 'open gmail' or query_ask == 'open mail' or query_ask == 'open my mail' or query_ask == 'my mailbox' or query_ask == 'what about my mailbox' or query_ask == 'got something new in my mailbox' or query_ask == 'update my mailbox' or query_ask == 'someting new in my mail' or query_ask == 'got something new in my mail' :
                stMsgs = ['opening email','ok processing ... your request ....','please wait... your request is being processed','ok','getting you to your mailbox','forwording you to your mail']
                speak(random.choice(stMsgs))
                webbrowser.open('www.gmail.com')

            elif query_ask == 'news' or query_ask =='news please' or query_ask == 'tell me some news'  or query_ask == 'kindly tell me some news' or query_ask == 'get me some news' or query_ask == 'update me with news' or query_ask == 'update me with whats going across world' or query_ask == 'whats is going around' or query_ask == 'got someting from across world':
                stMsgs = ['Telling news','ok processing ... your request ....','please wait... your request is being processed','ok','getting you some news' ,'this is whats going aroud']
                speak(random.choice(stMsgs))
                news()

            elif query_ask == 'what is your name' or query_ask == 'tell me your name' or query_ask == 'your name please' or query_ask == 'what about you' :
                speak('my name is jarvis sir')
                speak('i am your degital assistant')
                stMsgs = ['how can i help you','let me help you','may you need my help','i try just to help my user']
                speak(random.choice(stMsgs))
            
            elif query_ask == 'tell me about yourself' or query_ask == 'give me your intro' or query_ask == 'your intro' or query_ask == 'your intro please' or query_ask == 'tell me something about you' or query_ask == 'who made you' or query_ask == 'who is your creator' or query_ask == 'who is your god':
                speak('actually i am a program currently under development')
                speak('i do not have any specific name but you can call me Jarvis')
                speak('so technically my name is jarvis sir')
                speak('i am your degital assistant')
                speak('i am under development by the Santosh ')
                stMsgs = ['how can i help you','let me help you','may you need my help','please let me know how can i be useful','just trying to help','wanna some help']
                speak(random.choice(stMsgs))

            elif query_ask == 'jarvis' or query_ask == 'are you listening me' or query_ask == 'jarvis are you online' or query_ask == 'are you active now' or query_ask == 'jarvis are you ready' or query_ask == 'jarvis i need your help' or query_ask == 'jarvis can you help me':
                speak('yes sir')
                speak('i am resay and online now')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))

            elif query_ask == 'where is your home' or query_ask == 'where do you live' or query_ask == 'your address please' or query_ask == 'tell me your address' or query_ask == 'tell me your address please': 
                stMsgs = ['thank you for asking such a intro','thank you sir for such question','i am glad to know that you want to know about me']
                speak(random.choice(stMsgs))
                speak('thank you for asking such a intro')
                speak('i am your degital assistant')
                speak('i am under development by the Santosh ')
                speak('currently i don\'n have any home')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))

            elif query_ask == "what\'s up" or query_ask == 'how are you' or query_ask == 'what about you' or query_ask=='':
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy' , 'i am feeloing chilled waht about you sir']
                speak(random.choice(stMsgs))

            elif query_ask == 'thanks' or query_ask == 'thank you jarvis' or query_ask == 'thank you' or query_ask == 'thank you for help' or query_ask == 'thank you for doing my things' or query_ask == 'thanks fro help' :
                stMsgs = ['welcome sir','same to you sir','welcome to you sir']
                speak(random.choice(stMsgs))
                stMsgs = ['Just doing my things!','just doing my jobs sir', 'no need to say thanks sir', 'same to you sir', 'thank you sir i am nice and full of energy' , 'i am feeloing chilled now sir what abou you sir']
                speak(random.choice(stMsgs))
                
            elif query_ask == 'thanks for help ' or query_ask  == 'thaks you so much' or query_ask == 'thank for all jarvis' or query_ask == 'thaks jarvis' :
                stMsgs = ['welcome sir','same to you sir','welcome to you sir']
                speak(random.choice(stMsgs))
                stMsgs = ['Just doing my things!','just doing my jobs sir', 'no need to say thanks sir', 'same to you sir', 'thank you sir i am nice and full of energy' , 'i am feeloing chilled now sir what abou you sir']
                speak(random.choice(stMsgs))




            elif query_ask == 'email' or query_ask == 'send email' or query_ask == 'send mail' :
                speak('Who is the recipient? ')
                recipient = myCommand()

                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(username,password)
                    server.sendmail(username, recipient+'@gmail.com', content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry sir! I am unable to send your message at this moment!')


            elif query_ask =='nothing' or query_ask == 'exit' or query_ask == 'abort' or query_ask == 'stop' or query_ask == 'go away' or query_ask == 'quit' or query_ask == 'good by' :
                speak('okay')
                speak('Bye sir, have a good day.')
                break
                sys.exit()
            

            elif query_ask  == 'what is the time now' or query_ask == 'tell me the time' or query_ask == 'tell me systam time' or query_ask == 'time now':
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"sir, the time is {strTime}")
                
            
            elif query_ask == 'hello' or query_ask == 'hi' or query_ask == 'hii' or query_ask == 'hy' or query_ask == 'hyy' :
                hiMsgs = ['hello','hii','hi','hy','hello sir']
                speak(random.choice(hiMsgs))

            elif 'bye' in query_ask or 'byy' in query_ask or query_ask == 'by' :
                speak('Bye sir, have a good day.')
                break
                sys.exit()
                                        
            elif 'play music' in query_ask or 'play song' in query_ask or 'play my favourite song' in query_ask :
                stMsgs = ['opening songs','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                webbrowser.open('https://music.youtube.com')
                
                    

            elif query_ask == 'jokes' or query_ask == 'tell me a joke' or query_ask == 'speak me joke' or query_ask == 'speak joke':
                speak(pyjokes.get_joke(category='all'))
            
            elif query_ask == 'restart' or query_ask == 'restart my PC' or query_ask == 'please restart my PC' or query_ask == 'please restart' or query_ask == 'reboot' or query_ask == 'reboot my PC ' or query_ask == 'restart my computer' or query_ask == 'reboot my computer':
                speak('Rebooting')
                os.system("shutdown -t 10 -r -f") 
                break
                sys.exit()

            elif query_ask == 'shutdown' or query_ask == 'shutdown my PC' or query_ask == 'please shutdown my PC' or query_ask == 'please shutdown' or query_ask == 'shutdown my computer' or query_ask == 'shutdown my computer':
                speak('Rebooting')
                os.system("shutdown -t 10 -s -f")
                break
                sys.exit()

            elif 'search for on google' in query_ask or 'search on google for' in query_ask or 'ask google for' in query_ask :
                stMsgs = ['opening google','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                if 'search for on google ' in query_ask :
                    query_ask=query_ask.replace("search for on google",'')
                elif 'search on google for' in query_ask :
                    query_ask = query_ask.replace('search on google for','')
                elif 'ask google for' in query_ask:
                    query_ask = query_ask.replace('ask google for','')
                webbrowser.open('https://www.google.com/search?q='+query_ask)

            elif 'search for on youtube' in query_ask :
                stMsgs = ['opening youtube','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                if 'search for on youtube ' in query_ask :
                    query_ask=query_ask.replace("search for on youtube",'')
                elif 'search on youtube for' in query_ask :
                    query_ask = query_ask.replace('search on youtube for','')
                webbrowser.open('https://www.youtube.com/results?search_query='+query_ask)

            else:
            
                speak('Searching...')
                try:
                    try:
                        res = client.query(query_ask)
                        results = next(res.results).text
                        speak('I got this !!!')
                        speak(results)
                        
                    except:
                        results = wikipedia.summary(query_ask, sentences=2)
                        speak('Got it.')
                        speak('WIKIPEDIA says - ')
                        speak(results)
            
                except:
                    webbrowser.open('https://www.google.com/search?q='+query_ask)
            
            speak('Next Command! sir!')
except:
    print('An error occured kindly restart the program') 
    sy=input("Hit enter to exit ")
    sys.exit()
