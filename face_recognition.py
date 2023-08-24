from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")
        
        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=50)
        #first image
        img_top=Image.open(r"E:\Face Recognition\college_images\face_detector1.jpg")
        img_top=img_top.resize((650,650),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=650)
        
        #second image
        bg1=Image.open(r"E:\Face Recognition\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        bg1=bg1.resize((950,650),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

       
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=620,y=55,width=950,height=650)
        
        std_b1 = Button(bg_img,command=self.face_recog,text="Face Recognition",cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        std_b1.place(x=370,y=550,width=200,height=40)
    #attendance=====================
    
    def mark_attendance(self,i,r,n):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
#==============Face Recognition===========
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host='localhost',port='3306',username='root',password='',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute("select student_name from student where stu_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select roll_no from student where stu_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select department from student where stu_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord  
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
         

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()