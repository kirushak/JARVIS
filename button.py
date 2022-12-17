from tkinter import*

tk=Tk()
def initiate():
    print("Welcome to JARVIS!!,Your personalized AI chatbot :)")
    btn['text']="STARTED" #letters that would be displayed after the button gets
                           #freezed
    btn['state']= 'disabled' #the user cant click the button again
    #functions needed from source code to make jarvis respond
    

#terminate

    

tk1=Tk()
def end():
        
    print("THANK YOU FOR AVAILING THE SERVICE")
    btn1["text"]="ENDED"
    btn1['state']='disabled'
   
ex=input("Dou you wanna start? (yes/no) : ")
if ex in ["no","NO","No"]:
    btn1= Button(tk,text = "CLICK HERE TO TERMINATE",command=end)
    btn1.pack()
    #code to terminate jarvis
else:
    btn=Button(tk,text="CLICK HERE TO START",command =initiate)
    btn.pack()
    #call jarvis
    
    
    
    
   





