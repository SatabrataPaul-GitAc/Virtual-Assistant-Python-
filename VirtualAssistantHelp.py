
import pyttsx3
import os
pyttsx3.speak("Welcome to tools ")
pyttsx3.speak("You can chat with me on what you would like to open on your pc or laptop")
pyttsx3.speak("Whenever your requirement is fullfilled you can write exit or done to end your conversation")
while True:
    print("Enter your requirement :",end='')
    user=input()
    if ('done' in user  or 'exit' in user):
        break
    if ('chrome' in user):
        if ((("don't" in user) or ("donot" in user))and(("run" in user) or ("open" in user) or ("launch" in user))):
            print("OK your program is not launched !")
            pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
        elif(("run" in user) or ("open" in user) or ("launch" in user)):
            os.system("chrome")
            pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
        else:
            pyttsx3.speak("Did you mean to open chrome browser ?")
            b=input("Enter a yes or no :")
            b=b.upper()
            if(b=="YES"):
                os.system("chrome")
                pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
            elif(b=="NO"):
                print("OK Your requirement is fulfilled . Chrome browser is not launched !")
                pyttsx3.speak("You can continue with your next requirement")
            else:
                print("Your input was invalid !")
    elif (("notepad" in user)or("text editor" in user)or("editor" in user)):
        if (("don't" in user) or ("donot" in user)):
            print("OK your program is not launched !")
            pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
        elif(("run" in user) or ("open" in user) or ("launch" in user)):
            os.system("notepad")
            pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")

        else:
            pyttsx3.speak("Did you mean to open notepad text editor ?")
            b=input("Enter a yes or no :")
            b=b.upper()
            if(b=="YES"):
                os.system("notepad")
                pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
            elif(b=="NO"):
                print("OK Your requirement is fulfilled . Notepad is not launched !")
                pyttsx3.speak("You can continue with your next requirement")
            else:
                print("Your input was invalid !")
    elif ("firefox" in user):
        if (("don't" in user) or ("donot" in user)):
            print("OK your program is not launched !")
            pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
        elif(("run" in user) or ("open" in user) or ("launch" in user)):
            os.system("firefox")
            pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
        else:
            pyttsx3.speak("Did you mean to open firefox browser ?")
            b=input("Enter a yes or no :")
            b=b.upper()
            if(b=="YES"):
                os.system("firefox")
                pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
            elif(b=="NO"):
                print("OK Your requirement is fulfilled . Firefox browser is not launched !")
                pyttsx3.speak("You can continue with your next requirement")
            else:
                print("Your input was invalid !")
    elif (("media player" in user)or("player" in user)):
        if (("don't" in user) or ("donot" in user)):
            print("OK your program is not launched !")
            pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
        elif(("run" in user) or ("open" in user) or ("launch" in user)):
            os.system("KMPlayer")
            pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
        else:
            pyttsx3.speak("Did you mean to open KM media player ?")
            b=input("Enter a yes or no :")
            b=b.upper()
            if(b=="YES"):
                os.system("KMPlayer")
                pyttsx3.speak("Requirement fullfilled . You can continue with your next requirement")
            elif(b=="NO"):
                print("OK Your requirement is fulfilled . KM Player is not launched !")
                pyttsx3.speak("You can continue with your next requirement")
            else:
                print("Your input was invalid !")
    else:
        pyttsx3.speak("The program is not available in your system")
pyttsx3.speak("Thank You for conversing ! Hope to see you again")
