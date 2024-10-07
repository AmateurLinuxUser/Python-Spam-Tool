import os
import pyautogui
import time

def spam(message, n, gap) :
    time.sleep(3)
    i = 1
    while i <= n :
        pyautogui.write(message)
        pyautogui.press('enter')
        time.sleep(gap)
        i = i + 1

n = 0
message = ""
gap = 0.1
menu = ""

while menu != "0" :
    if os.name == 'nt' :
        os.system("cls")
    else :
        os.system("clear")

    print("""\033[1;34;40m
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ███████╗██████╗  █████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    ███████╗██████╔╝███████║██╔████╔██║       ██║   ██║   ██║██║   ██║██║     
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ███████║██║     ██║  ██║██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
\033[0;37;40m""")

    print(f"""*Current Information : N = {n}, Message = {message}, Gap : {gap} seconds
    Option : 
    [1] Input N
    [2] Input Message
    [3] Set Gap
    [4] Attack
    [0] Exit""")
    menu = input(">>> ")
    if(menu == "1") :
        n = int(input("Masukan nilai n : "))
    elif(menu == "2") :
        message = input("Masukan pesan : ")
    elif(menu == "3") :
        gap = float(input("Masukan gap : "))
    elif(menu == "4") :
        spam(message, n, gap)
    elif(menu == "0") :
        print("Exit...")
    else :
        print("Not Found")