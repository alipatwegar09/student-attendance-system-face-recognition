from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition

from attendance import Attendance
class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1535x780+0+0")
        self.root.title("Face Recognition System")
        #first image
        img=Image.open(r"E:\Face Recognition\college_images\bg1.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=500,height=130)
        #second image
        img1=Image.open(r"E:\Face Recognition\college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=500,y=0,width=500,height=130)
        #third image
        img2=Image.open(r"E:/Face Recognition/college_images/bg.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=1000,y=0,width=500,height=130)
        
        #bg img
        img3=Image.open(r"E:\Face Recognition\college_images\background.jpg")
        img3=img3.resize((1520,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1520,height=700)
        
        title_lbl=Label(bg_img,text="Real Time Presence Tracking Software By Face Recognition",font=("times new roman",28,"bold"),bg="white",fg="magenta")
        title_lbl.place(x=0,y=0,width=1530,height=47)
        
        #student button
        img4=Image.open(r"E:\Face Recognition\college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor='hand2')
        b1.place(x=180,y=90,width=220,height=200)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=180,y=270,width=220,height=40)
        
        #Detect face
        img5=Image.open(r"E:\Face Recognition\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor='hand2',command=self.face_detector)
        b1.place(x=460,y=90,width=220,height=200)
        
        b1_1=Button(bg_img,text="Face Detector",cursor='hand2',command=self.face_detector,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=460,y=270,width=220,height=40)
        
        #Attendence 
        img6=Image.open(r"E:\Face Recognition\college_images\abc.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor='hand2')
        b1.place(x=740,y=90,width=220,height=200)
        
        b1_1=Button(bg_img,text="Presence Record",command=self.attendence,cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=740,y=270,width=220,height=40)
        
        #ChatBot
        img7=Image.open(r"E:\Face Recognition\college_images\chat.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor='hand2')
        b1.place(x=1000,y=90,width=220,height=200)
        
        b1_1=Button(bg_img,text="ChatBot",cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=270,width=220,height=40)
        
        #TRAIN FACE
        img8=Image.open(r"E:\Face Recognition\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor='hand2',command=self.train_data)
        b1.place(x=180,y=330,width=220,height=200)
        
        b1_1=Button(bg_img,text="Train Data",cursor='hand2',command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=180,y=520,width=220,height=40)
        
        #Photos button
        img9=Image.open(r"E:\Face Recognition\college_images\IMG_1183_augmented_reality_faces1.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor='hand2')
        b1.place(x=460,y=330,width=220,height=200)
        
        b1_1=Button(bg_img,text="All Photos",cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=460,y=520,width=220,height=40)
        
        #Developers 
        img10=Image.open(r"E:\Face Recognition\college_images\developer.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor='hand2')
        b1.place(x=740,y=330,width=220,height=200)
        
        b1_1=Button(bg_img,text="Developers",cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=740,y=520,width=220,height=40)
        
        #Exit
        img11=Image.open(r"E:\Face Recognition\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,command=self.Close,image=self.photoimg11,cursor='hand2')
        b1.place(x=1000,y=330,width=220,height=200)
        
        b1_1=Button(bg_img,command=self.Close,text="Exit",cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=520,width=220,height=40)
        
    def open_img(self):
        os.startfile("Data")
        
        
#------------------Function buttons---------------

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_detector(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendence(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def Close(self):
        root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()