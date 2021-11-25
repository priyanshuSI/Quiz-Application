import tkinter as tk
from tkinter import IntVar
from tkinter import messagebox
from PIL import Image,ImageTk

percentage,score=0,0       
responses = [-1]*5
answers = [1,2,1,4,3]
def go_to_result(controller):
    res = messagebox.askquestion('Exit Application','Do you really want to exit?',default="no") 
    if res == 'yes' :
        controller.show_frame(EighthPage)
        
class FirstPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        load = Image.open("12.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image=photo
        label.place(x=0,y=0)        
        
        border=tk.LabelFrame(self,text="Login",font=("Arial",23),bd=7,bg="#73A5C6")
        border.pack(fill="both",expand="yes",padx=420,pady=190)
        
        l1=tk.Label(border,text="Username: ",font=("Arial",17),bg="light blue")
        l1.place(x=70,y=30)
        t1=tk.Entry(border,width=40,bd=7)
        t1.place(x=200,y=30)
        
        l2=tk.Label(border,text="Password: ",font=("Arial",17),bg="light blue")
        l2.place(x=70,y=100)
        t2=tk.Entry(border,width=40,bd=7,show="*")
        t2.place(x=200,y=100)        
        
        def verify():
            if t1.get()!="" and t2.get()!="":
                with open("credintial1.txt","r") as f:
                    info=f.readlines()
                    i=0
                    for e in info:
                        u,p=e.split(",")
                        if u.strip()== t1.get() and p.strip()== t2.get():
                            controller.show_frame(SecondPage)
                            i=1
                            break
                    if i==0:
                        messagebox.showinfo("Error","Please provide correct Username and Password!!")    
            else:
                messagebox.showinfo("Error", "Please fill Username and Password!!")    
        b1=tk.Button(border,text="SUBMIT",font=("Arial",17,"bold"),bd=7,bg="#2196F3",fg="white",command=verify)
        b1.place(x=240,y=162)
        
        def register():
            window=tk.Tk()
            window.title("Register")
            window.resizable(0,0)
            window.configure(bg="deep sky blue")
            
            l1=tk.Label(window,text="Username: ",font=("Arial",17),bg="deep sky blue")
            l1.place(x=30,y=30)
            t1=tk.Entry(window,width=40,bd=7)
            t1.place(x=240,y=30)
            
            l2=tk.Label(window,text="Password: ",font=("Arial",17),bg="deep sky blue")
            l2.place(x=30,y=80)
            t2=tk.Entry(window,width=40,bd=7,show="*")
            t2.place(x=240,y=80)
            
            l3=tk.Label(window,text="Confirm Password: ",font=("Arial",17),bg="deep sky blue")
            l3.place(x=30,y=130)
            t3=tk.Entry(window,width=40,bd=7,show="*")
            t3.place(x=240,y=130)
            
            def check():
                if t1.get()!="" and t2.get()!="" and t3.get()!="":
                    if t2.get() == t3.get():
                        with open("credintial1.txt","a") as f:
                            f.write(t1.get()+","+t2.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error","Password and Confirm Password should be same!!")
                else:
                    messagebox.showinfo("Error","Please fill the complete fields!!")        
            b1=tk.Button(window,text="Sign In",font=("Arial",17,"bold"),bd=7,bg="orange",command=check) 
            b1.place(x=200,y=190) 
            
            window.geometry("560x270")
            window.mainloop()
        b2=tk.Button(self,text="Register",font=("Arial",18,"bold"),bd=7,bg="dark orange",command=register)
        b2.place(x=1100,y=50)                         
                
class SecondPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        f1=tk.Frame(self,height=50,width=1400,bg="light blue")
        f1.place(x=0,y=0)
        l1=tk.Label(f1,text="Instructions",font=("Arial",20,"bold"),bg="light blue")
        l1.place(x=610,y=6)
        
        f2=tk.Frame(self,height=600,width=1400,bg="white")
        f2.place(x=0,y=50)
        l2=tk.Label(f2,text="Read all the instructions carefully before attempting the test.",font=("Arial",13,"italic"),bg="white")
        l2.place(x=220,y=47)
        l3=tk.Label(f2,text="1. There are 5 Multiple Choice Questions.",font=("Arial",14),bg="white")
        l3.place(x=50,y=120)
        l4=tk.Label(f2,text="2. Every Question carry 1 Marks.",font=("Arial",14),bg="white")
        l4.place(x=50,y=155)
        l5=tk.Label(f2,text="3. There is a NEGATIVE MARKING of -25%(0.25 marks on every question).",font=("Arial",14),bg="white")
        l5.place(x=50,y=190)
        l6=tk.Label(f2,text="4. Once you click on NEXT button, you will not be able to come back to that question later.",font=("Arial",14),bg="white")
        l6.place(x=50,y=225)
        l7=tk.Label(f2,text="5. Press the END TEST button only when you have completed the test.",font=("Arial",14),bg="white")
        l7.place(x=50,y=260)
        l8=tk.Label(f2,text="6. No marks will be deducted for skipping the questions.",font=("Arial",14),bg="white")
        l8.place(x=50,y=295)
        l9=tk.Label(f2,text="ALL THE BEST",font=("Arial",20),bg="white")
        l9.place(x=530,y=390)
        
        b1=tk.Button(self,text="Back",font=("Arial",14,"bold"),bd=5,bg="red",fg="white",pady=5,padx=3,command=lambda:controller.show_frame(FirstPage))
        b1.place(x=50,y=550)
        b2=tk.Button(self,text="Proceed",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=lambda:controller.show_frame(ThirdPage))
        b2.place(x=1250,y=550)

class ThirdPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent) 
        
        b1=tk.Button(self,text="End Test",font=("Arial",14,"bold"),bd=5,bg="red",fg="white",pady=5,padx=3,command=lambda:go_to_result(controller))
        b1.place(x=50,y=550)
        
        b2=tk.Button(self,text="Next",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=lambda:controller.show_frame(FourthPage))
        b2.place(x=1270,y=550)
        
        def clear_response():
            responses[0]=-1
            var.set(None)
        b3=tk.Button(self,text="Clear Response",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=clear_response)
        b3.place(x=200,y=550)
        
        f1=tk.Frame(self,height=50,width=1400,bg="orange")
        f1.place(x=0,y=0)
        l1=tk.Label(f1,text="Question: 1 of 5",font=("Arial",12),padx=30,pady=3)
        l1.place(x=60,y=10)
        l2=tk.Label(f1,text="Marks for this Question: 1",font=("Arial",12),padx=50,pady=3)
        l2.place(x=450,y=10)        
        l3=tk.Label(f1,text="Negative Marks: -25% on wrong answer",font=("Arial",12),padx=50,pady=3)
        l3.place(x=950,y=10)

        f2=tk.Frame(self,height=100,width=1400,bg="light blue")
        f2.place(x=0,y=50)
        l1=tk.Label(f2,text="Q.1 - ",font=("Arial",25,"italic"),pady=10,bg="light blue")
        l1.place(x=15,y=15)          
        l2=tk.Label(f2,text="Which of the following is not a keyword in python?",font=("Arial",25,"bold"),padx=20,pady=10)
        l2.place(x=100,y=15) 
        
        f3=tk.Frame(self,height=350,width=1400,bg="white")
        f3.place(x=0,y=150)
        var=IntVar()
        
        def collect_response():
            responses[0]=var.get()    
        r1=tk.Radiobutton(f3,text="true",font=("Arial",20),bg="white",variable=var,value=1,pady=5, command=collect_response)
        r1.place(x=20,y=30)
        r2=tk.Radiobutton(f3,text="False",font=("Arial",20),bg="white",variable=var,value=2,pady=5, command=collect_response)
        r2.place(x=20,y=100)
        r3=tk.Radiobutton(f3,text="else",font=("Arial",20),bg="white",variable=var,value=3,pady=5, command=collect_response)
        r3.place(x=20,y=170)
        r4=tk.Radiobutton(f3,text="for",font=("Arial",20),bg="white",variable=var,value=4,pady=5, command=collect_response)
        r4.place(x=20,y=240) 
        
        
class FourthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        b1=tk.Button(self,text="End Test",font=("Arial",14,"bold"),bd=5,bg="red",fg="white",pady=5,padx=3,command=lambda:go_to_result(controller))
        b1.place(x=50,y=550)
        
        b2=tk.Button(self,text="Next",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=lambda:controller.show_frame(FifthPage))
        b2.place(x=1270,y=550)
        
        def clear_response():
            responses[1]=-1
            var.set(None)
        b3=tk.Button(self,text="Clear Response",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=clear_response)
        b3.place(x=200,y=550)
        
        f1=tk.Frame(self,height=50,width=1400,bg="orange")
        f1.place(x=0,y=0)
        l1=tk.Label(f1,text="Question: 2 of 5",font=("Arial",12),padx=30,pady=3)
        l1.place(x=60,y=10)
        l2=tk.Label(f1,text="Marks for this Question: 1",font=("Arial",12),padx=50,pady=3)
        l2.place(x=450,y=10)        
        l3=tk.Label(f1,text="Negative Marks: -25% on wrong answer",font=("Arial",12),padx=50,pady=3)
        l3.place(x=950,y=10)

        f2=tk.Frame(self,height=100,width=1400,bg="light blue")
        f2.place(x=0,y=50)
        l1=tk.Label(f2,text="Q.2 - ",font=("Arial",25,"italic"),pady=10,bg="light blue")
        l1.place(x=15,y=15)          
        l2=tk.Label(f2,text="Which one of the following is the correct extension of the Python file?",font=("Arial",25,"bold"),padx=20,pady=10)
        l2.place(x=100,y=15) 
        
        f3=tk.Frame(self,height=350,width=1400,bg="white")
        f3.place(x=0,y=150)
        var=IntVar()
        def collect_response():
            responses[1]=var.get()
        r1=tk.Radiobutton(f3,text=".python",font=("Arial",20),bg="white",variable=var,value=1,pady=5, command=collect_response)
        r1.place(x=20,y=30)
        r2=tk.Radiobutton(f3,text=".py",font=("Arial",20),bg="white",variable=var,value=2,pady=5, command=collect_response)
        r2.place(x=20,y=100)
        r3=tk.Radiobutton(f3,text=".pl",font=("Arial",20),bg="white",variable=var,value=3,pady=5, command=collect_response)
        r3.place(x=20,y=170)
        r4=tk.Radiobutton(f3,text=".p",font=("Arial",20),bg="white",variable=var,value=4,pady=5, command=collect_response)
        r4.place(x=20,y=240)
        
        
class FifthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        b1=tk.Button(self,text="End Test",font=("Arial",14,"bold"),bd=5,bg="red",fg="white",pady=5,padx=3,command=lambda:go_to_result(controller))
        b1.place(x=50,y=550)
        
        b2=tk.Button(self,text="Next",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=lambda:controller.show_frame(SixthPage))
        b2.place(x=1270,y=550)
        
        def clear_response():
            responses[2]=-1
            var.set(None)
        b3=tk.Button(self,text="Clear Response",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=clear_response)
        b3.place(x=200,y=550)
        
        f1=tk.Frame(self,height=50,width=1400,bg="orange")
        f1.place(x=0,y=0)
        l1=tk.Label(f1,text="Question: 3 of 5",font=("Arial",12),padx=30,pady=3)
        l1.place(x=60,y=10)
        l2=tk.Label(f1,text="Marks for this Question: 1",font=("Arial",12),padx=50,pady=3)
        l2.place(x=450,y=10)        
        l3=tk.Label(f1,text="Negative Marks: -25% on wrong answer",font=("Arial",12),padx=50,pady=3)
        l3.place(x=950,y=10)

        f2=tk.Frame(self,height=100,width=1400,bg="light blue")
        f2.place(x=0,y=50)
        l1=tk.Label(f2,text="Q.3 - ",font=("Arial",25,"italic"),pady=10,bg="light blue")
        l1.place(x=15,y=15)          
        l2=tk.Label(f2,text="Which of the following is used to define a block of code in Python language?",font=("Arial",25,"bold"),padx=20,pady=10)
        l2.place(x=100,y=15) 
        
        f3=tk.Frame(self,height=350,width=1400,bg="white")
        f3.place(x=0,y=150)
        var=IntVar()
        def collect_response():
            responses[2]=var.get()
        r1=tk.Radiobutton(f3,text="Indentation",font=("Arial",20),bg="white",variable=var,value=1,pady=5, command=collect_response)
        r1.place(x=20,y=30)
        r2=tk.Radiobutton(f3,text="Key",font=("Arial",20),bg="white",variable=var,value=2,pady=5, command=collect_response)
        r2.place(x=20,y=100)
        r3=tk.Radiobutton(f3,text="Brackets",font=("Arial",20),bg="white",variable=var,value=3,pady=5, command=collect_response)
        r3.place(x=20,y=170)
        r4=tk.Radiobutton(f3,text="All of the mentioned",font=("Arial",20),bg="white",variable=var,value=4,pady=5, command=collect_response)
        r4.place(x=20,y=240)  
        
        
class SixthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        b1=tk.Button(self,text="End Test",font=("Arial",14,"bold"),bd=5,bg="red",fg="white",pady=5,padx=3,command=lambda:go_to_result(controller))
        b1.place(x=50,y=550)
        
        b2=tk.Button(self,text="Next",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=lambda:controller.show_frame(SeventhPage))
        b2.place(x=1270,y=550)
        
        def clear_response():
            responses[3]=-1
            var.set(None)
        b3=tk.Button(self,text="Clear Response",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=clear_response)
        b3.place(x=200,y=550)
        
        f1=tk.Frame(self,height=50,width=1400,bg="orange")
        f1.place(x=0,y=0)
        l1=tk.Label(f1,text="Question: 4 of 5",font=("Arial",12),padx=30,pady=3)
        l1.place(x=60,y=10)
        l2=tk.Label(f1,text="Marks for this Question: 1",font=("Arial",12),padx=50,pady=3)
        l2.place(x=450,y=10)        
        l3=tk.Label(f1,text="Negative Marks: -25% on wrong answer",font=("Arial",12),padx=50,pady=3)
        l3.place(x=950,y=10)

        f2=tk.Frame(self,height=100,width=1400,bg="light blue")
        f2.place(x=0,y=50)
        l1=tk.Label(f2,text="Q.4 - ",font=("Arial",25,"italic"),pady=10,bg="light blue")
        l1.place(x=15,y=15)          
        l2=tk.Label(f2,text="Which keyword is used for function in Python language?",font=("Arial",25,"bold"),padx=20,pady=10)
        l2.place(x=100,y=15) 
        
        f3=tk.Frame(self,height=350,width=1400,bg="white")
        f3.place(x=0,y=150)
        var=IntVar()
        def collect_response():
            responses[3]=var.get()
        r1=tk.Radiobutton(f3,text="Function",font=("Arial",20),bg="white",variable=var,value=1,pady=5, command=collect_response)
        r1.place(x=20,y=30)
        r2=tk.Radiobutton(f3,text="Fun",font=("Arial",20),bg="white",variable=var,value=2,pady=5, command=collect_response)
        r2.place(x=20,y=100)
        r3=tk.Radiobutton(f3,text="Def",font=("Arial",20),bg="white",variable=var,value=3,pady=5, command=collect_response)
        r3.place(x=20,y=170)
        r4=tk.Radiobutton(f3,text="def",font=("Arial",20),bg="white",variable=var,value=4,pady=5, command=collect_response)
        r4.place(x=20,y=240)  
        
        
class SeventhPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        b1=tk.Button(self,text="End Test",font=("Arial",14,"bold"),bd=5,bg="red",fg="white",pady=5,padx=3,command=lambda:controller.show_frame(EighthPage))
        b1.place(x=50,y=550)
        
        def clear_response():
            responses[4]=-1
            var.set(None)
        b3=tk.Button(self,text="Clear Response",font=("Arial",14,"bold"),bd=5,bg="#2196F3",fg="white",pady=5,padx=3,command=clear_response)
        b3.place(x=200,y=550)
        
        f1=tk.Frame(self,height=50,width=1400,bg="orange")
        f1.place(x=0,y=0)
        l1=tk.Label(f1,text="Question: 5 of 5",font=("Arial",12),padx=30,pady=3)
        l1.place(x=60,y=10)
        l2=tk.Label(f1,text="Marks for this Question: 1",font=("Arial",12),padx=50,pady=3)
        l2.place(x=450,y=10)        
        l3=tk.Label(f1,text="Negative Marks: -25% on wrong answer",font=("Arial",12),padx=50,pady=3)
        l3.place(x=950,y=10)

        f2=tk.Frame(self,height=100,width=1400,bg="light blue")
        f2.place(x=0,y=50)
        l1=tk.Label(f2,text="Q.5 - ",font=("Arial",25,"italic"),pady=10,bg="light blue")
        l1.place(x=15,y=15)          
        l2=tk.Label(f2,text="Which of the following character is used to give single-line comments in Python?",font=("Arial",25,"bold"),padx=15,pady=10)
        l2.place(x=100,y=15) 
        
        f3=tk.Frame(self,height=350,width=1400,bg="white")
        f3.place(x=0,y=150)
        var=IntVar()
        def collect_response():
            responses[4]=var.get()
        r1=tk.Radiobutton(f3,text="//",font=("Arial",20),bg="white",variable=var,value=1,pady=5, command=collect_response)
        r1.place(x=20,y=30)
        r2=tk.Radiobutton(f3,text="!",font=("Arial",20),bg="white",variable=var,value=2,pady=5, command=collect_response)
        r2.place(x=20,y=100)
        r3=tk.Radiobutton(f3,text="#",font=("Arial",20),bg="white",variable=var,value=3,pady=5, command=collect_response)
        r3.place(x=20,y=170)
        r4=tk.Radiobutton(f3,text="/*",font=("Arial",20),bg="white",variable=var,value=4,pady=5, command=collect_response)
        r4.place(x=20,y=240)  
        
        
class EighthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="light blue") 
        
        b1=tk.Button(self,text="Home",font=("Arial",14,"bold"),bd=5,bg="orange",fg="white",pady=5,padx=3,command=lambda: controller.show_frame(FirstPage))
        b1.place(x=1270,y=550)
        
        f1=tk.Frame(self,height=60,width=1400,bg="orange")
        f1.place(x=0,y=0)
        l1=tk.Label(f1,text="Click on \"Show Result\" button to know your result ",font=("Arial",12),padx=30,pady=3)
        l1.place(x=520,y=18)       
        
        def calculate_result():
            n_correct,n_wrong=0,0
            for i in range (len(responses)):
                if(responses[i]==-1):
                    pass 
                elif(responses[i]==answers[i]):
                    n_correct+=1
                else:
                    n_wrong+=1
            global score, percentage
            score=n_correct-0.25*n_wrong  
            percentage=score*100/len(responses)
            l1=tk.Label(self,text=f"Your score is: {score} marks out of 5",font=("Arial",17,"bold"),padx=15,pady=5)
            l1.place(x=100,y=150) 
            l2=tk.Label(self,text=f"You secured: {percentage}%",font=("Arial",17,"bold"),padx=15,pady=5)
            l2.place(x=100,y=220)
        f2=tk.Frame(self,height=70,width=1400,bg="ivory")
        f2.place(x=0,y=60)     
        b2=tk.Button(f2,text="Show Result",font=("Arial",14,"bold"),bd=5,bg="red",fg="white",pady=5,padx=3,command=calculate_result)
        b2.place(x=650,y=10)  
        l3=tk.Label(self,text='"Keep up the good work"',font=("Arial",32,"bold"),bg="light blue",padx=15,pady=5)
        l3.place(x=430,y=400)    
         
 
class Application(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        window=tk.Frame(self) 
        window.pack()
        
        window.grid_rowconfigure(0,minsize=650)
        window.grid_columnconfigure(0,minsize=1400)
        
        self.frames={} 
        for F in (FirstPage, SecondPage, ThirdPage, FourthPage, FifthPage, SixthPage, SeventhPage, EighthPage):
            frame=F(window,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
            
        self.show_frame(FirstPage)    
        
    def show_frame(self,page):
        frame=self.frames[page]
        frame.tkraise()
        self.title("Quiz Application")
            
app=Application()
app.maxsize(1400,650)
app.mainloop()                              