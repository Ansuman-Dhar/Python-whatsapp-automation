import pyautogui, time, webbrowser, datetime
def send_mess(contact):
    f = open("chatscript.txt", 'r')

    print("Now take your hands away from mouse/ keyboard/ touchpad/ screen")
    print("This program will take over your PC to send the chat scripts")
    print('')
    time.sleep(7)

    webbrowser.open("https://web.whatsapp.com")
    print("Script will strart in 50 seconds")
    time.sleep(50)
    pyautogui.press("tab")
    pyautogui.typewrite(contact, interval=0.10)
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(1)

    for word in f:
        pyautogui.typewrite(word, interval=0.15)
        pyautogui.press("enter")


    print("script completed")
    print("Closing in 3 seconds")
    time.sleep(3)
    exit(0)

#waiting time = 60 secs
#total time = 63 secs