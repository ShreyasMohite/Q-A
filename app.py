from tkinter import *
import tkinter.messagebox
import threading
import os
from dotenv import load_dotenv  #pip install python-dotenv



class Questions:
    def __init__(self,root):
        self.root=root
        self.root.title("Questions and Answers") #title
        self.root.geometry("500x400")  #size of window
        self.root.iconbitmap("logo41.ico")  #adding icon on window
        self.root.resizable(0,0)    #no resizing of window

        ##creaing stringvar
        question=StringVar()

        load_dotenv()  #configuring dotenv
 
        
       


         #adding hover effect
        def on_enter1(e):
            but_Ask['background']="black"
            but_Ask['foreground']="cyan"
            
            

        def on_leave1(e):
            but_Ask['background']="SystemButtonFace"
            but_Ask['foreground']="SystemButtonText"


        def on_enter2(e):
            but_Clear['background']="black"
            but_Clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_Clear['background']="SystemButtonFace"
            but_Clear['foreground']="SystemButtonText"

        
        
        #function to ask question
        def askquestion():
            try:
                if len(question.get())==0:
                    tkinter.messagebox.showerror("Error","Please Enter Your Question")
                else:
                    import wolframalpha   #pip install wolframalpha
                    api_id=os.getenv('API_KEY')
                    client=wolframalpha.Client(api_id)
                    res=client.query(question.get())
                    answer=next(res.results).text
                    text.insert('end',answer)
            except Exception as e:
                print(e)
                tkinter.messagebox.showerror("Error","No Internet Connection,Please Connect to Internet")

        
        #threading question 
        def thread_question():
            t1=threading.Thread(target=askquestion)
            t1.start()

            






        #clear command for button
        def clear():
            text.delete(1.0,"end")
            question.set("")

#===========================frame========================
        
        #main window
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)
        
        #first question window
        questionframe=Frame(mainframe,width=494,height=200,relief="ridge",bd=3,bg="#78c9bf")
        questionframe.place(x=0,y=0)


        #second answer window which text
        answerframe=Frame(mainframe,width=494,height=195,relief="ridge",bd=3)
        answerframe.place(x=0,y=200)


#========================questionframe===================
        
        #label on top of fistframe
        QuesLabel=Label(questionframe,text="Ask Your Question Here",font=('times new roman',15),fg="black",bg="#78c9bf")
        QuesLabel.place(x=150,y=10)
        
        #adding Entry box for getting question
        QuesEntry=Entry(questionframe,width=40,font=('times new roman',15),bd=3,textvariable=question)
        QuesEntry.place(x=40,y=70)
        
        #button to perform action on question
        but_Ask=Button(questionframe,width=14,text="Ask",font=('times new roman',14),cursor="hand2",command=thread_question)
        but_Ask.place(x=50,y=130)
        but_Ask.bind("<Enter>",on_enter1)  #hover efffect on cursor over the button 
        but_Ask.bind("<Leave>",on_leave1)  #afte leaving cursor back to normal



        but_Clear=Button(questionframe,width=14,text="Clear",font=('times new roman',14),cursor="hand2",command=clear)
        but_Clear.place(x=290,y=130)
        but_Clear.bind("<Enter>",on_enter2) #hover efffect on cursor over the button
        but_Clear.bind("<Leave>",on_leave2) #afte leaving cursor back to normals

#========================Answerframe======================
        
        #creaing text for getting answer 
        text=Text(answerframe,width=53,height=8,font=('times new roman',14))
        text.place(x=3,y=9)
        





if __name__=="__main__":
    root=Tk()
    Questions(root)
    root.mainloop()