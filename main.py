import pyautogui, time, webbrowser, datetime
from functions import *

print("Make sure you have logged in to whatsapp web with 'keep me logged in' checked")
print("Make sure that you have his/her whatsapp number saved in your contacts")
print('')

print("Do you want to send this message(s) later?")
later_conf = input("Press 'y' for Yes OR 'n' for No: ")
if later_conf == "y":
    print("")
    t_day = input("The day on which the message has to be sent (In numbers): ")
    t_month = input("The month on which the message has to be sent (In numbers): ")
    t_year = input("The year on which the message has to be sent (In numbers): ")
    t_hour = input("The hour on which the message has to be sent (In 24-hours format): ")
    t_mins = input("The minute on which the message has to be sent (In numbers): ")
    t_date = datetime.datetime(int(t_year), int(t_month), int(t_day), int(t_hour), int(t_mins), 0)
    contact = input("\nName or whatsapp_number of reciever (country code is optional): ")

    CheckTime = True

    while CheckTime == True:
        c_day = int(datetime.datetime.now().day)
        c_month = int(datetime.datetime.now().month)
        c_year = int(datetime.datetime.now().year)
        c_hour = int(datetime.datetime.now().hour)
        c_mins = int(datetime.datetime.now().minute)
        c_date = datetime.datetime(c_year, c_month, c_day, c_hour, c_mins, 0)

        if c_date == t_date:
            send_mess(contact)
            CheckTime = False

else:
    print("Your message will be sent now")
    contact = input("\nName or whatsapp_number of reciever (country code is optional): ")
    print('')
    send_mess(contact)