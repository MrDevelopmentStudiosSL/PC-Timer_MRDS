import os
import time
from tkinter import messagebox

while True:
    try:
        print('''
|---------------------------------------------------------------------|
|                                                                     |
|                               PC Timer                              |
|                                                                     |
|            PC_TIMER v1.0 @ 2022 (C) MR Development Studios          |
|                                                                     |
|---------------------------------------------------------------------|
''')
        print('''
[1.] Shuttdown
[2.] Restart
[3.] Sign Out (Log Out)
[4.] Help
''')
        opt = int(input("Enter the Option Number : "))

        #Shuttdown
        if opt == 1:
            os.system('cls')
            print('<<<---------- ShuttDown ---------->>>\n')
            ttime = int(input("Enter the Time Range : "))
            unit = str(input("Enter the Unit : "))
            os.system('cls')
            print("Count Down was Started...\n")
            time.sleep(1)
            os.system('cls')
            if unit == 's' or unit == 'S':
                for second in range((ttime),0,-1):
                    print(f'{second} Seconds left')
                    time.sleep(1)
                    os.system('cls')
                messagebox.showwarning('Shuttdown', 'Your System Will Be Shutted Down')
                os.system('shutdown /s')
            elif unit == 'm' or unit == 'M':
                Range = ttime * 60
                for second in range((Range),0,-1):
                    print(f'{second} Seconds left')
                    time.sleep(1)
                    os.system('cls')
                messagebox.showwarning('Shuttdown', 'Your System Will Be Shutted Down')
                os.system('shutdown /s')
            elif unit == 'h' or unit == 'H':
                Range = ttime * 60 * 60
                for second in range((Range),0,-1):
                    print(f'{second} Seconds left')
                    time.sleep(1)
                    os.system('cls')
                messagebox.showwarning('Shuttdown', 'Your System Will Be Shutted Down')
                os.system('shutdown /s')


        #Restart
        elif opt == 2:
            os.system('cls')
            print('<<<---------- ReStart ---------->>>\n')
            ttime = int(input("Enter the Time Range : "))
            unit = str(input("Enter the Unit : "))
            os.system('cls')
            print("Count Down was Started...\n")
            time.sleep(1)
            os.system('cls')
            if unit == 's' or unit == 'S':
                for second in range((ttime),0,-1):
                    print(f'{second} Seconds left')
                    time.sleep(1)
                    os.system('cls')
                messagebox.showwarning('ReStart', 'Your System Will Be ReStarted')
                os.system('shutdown /r')
            elif unit == 'm' or unit == 'M':
                Range = ttime * 60
                for second in range((Range),0,-1):
                    print(f'{second} Seconds left')
                    time.sleep(1)
                    os.system('cls')
                messagebox.showwarning('ReStart', 'Your System Will Be ReStarted')
                os.system('shutdown /r')
            elif unit == 'h' or unit == 'H':
                Range = ttime * 60 * 60
                for second in range((Range),0,-1):
                    print(f'{second} Seconds left')
                    time.sleep(1)
                    os.system('cls')
                messagebox.showwarning('ReStarted', 'Your System Will Be ReStarted')
                os.system('shutdown /r')

        #Sign Out (LOG OUT)
        elif opt == 3:
            os.system('cls')
            print('<<<---------- Sign Out ---------->>>\n')
            ttime = int(input("Enter the Time Range : "))
            unit = str(input("Enter the Unit : "))
            os.system('cls')
            time.sleep(1)
            os.system('cls')
            print("Count Down was Started...\n")
            if unit == 's' or unit == 'S':
                for second in range((ttime),0,-1):
                    print(f'{second} Seconds left')
                    time.sleep(1)
                    os.system('cls')
                messagebox.showwarning('ReStart', 'Your System Will Be Signed Out')
                os.system('shutdown -l')
            elif unit == 'm' or unit == 'M':
                Range = ttime * 60
                for second in range((Range),0,-1):
                    print(f'{second} Seconds left')
                    time.sleep(1)
                    os.system('cls')
                messagebox.showwarning('ReStart', 'Your System Will Be Signed Out')
                os.system('shutdown -l')
            elif unit == 'h' or unit == 'H':
                Range = ttime * 60 * 60
                for second in range((Range),0,-1):
                    print(f'{second} Seconds left')
                    time.sleep(1)
                    os.system('cls')
                messagebox.showwarning('ReStart', 'Your System Will Be Signed Out')
                os.system('shutdown -l')

        #Help
        elif opt == 4:
            os.system('cls')
            print('''
< Help >

This Programme will helps you to manage your computer time and sava elecricity & time.

Time Units - S / s   -  Second
                   M / m  - Minutes
                   H / h   - Hours
''')
            input("Press Enter to Exit from HELP [ENTER]")
            os.system('cls')

        else:
            print('\nInvide Option number or Unknown Error\n')
            
    except:
        print('''
\nSomthing Went Wrong\n
''')
        os.system('cls')


# MR Development Studios
        
