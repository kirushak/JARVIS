import pywhatkit
import winshell
import time 
query=input("enter query:")
if 'play' in query:
    rquery = query.replace("play","")
    pywhatkit.playonyt(rquery)
elif 'empty recycle bin' in query:
    winshell.recycle_bin().empty(confirm=True,show_progress=True,sound=True)
elif 'time' in query:
    exacttime = time.strftime("%H:%M:%S", time.localtime())
    print(exacttime)