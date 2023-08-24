from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1535x780+0+0")
        self.root.title("Face Recognition System")
        
        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stu_id=StringVar()
        self.var_stu_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        #first image
        img=Image.open(r"E:\Face Recognition\college_images\face_recognition.png")
        img=img.resize((500,120),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=500,height=120)
        #second image
        img1=Image.open(r"E:\Face Recognition\college_images\gfd.jpg")
        img1=img1.resize((500,120),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=500,y=0,width=500,height=120)
        #third image
        img2=Image.open(r"E:/Face Recognition/college_images/bg.jpg")
        img2=img2.resize((500,120),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=1000,y=0,width=500,height=120)
        
        img3=Image.open(r"E:\Face Recognition\college_images\background.jpg")
        img3=img3.resize((1500,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1500,height=700)
        
        title_lbl=Label(bg_img,text="Student Panel",font=("times new roman",26,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1450,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1330,height=520)
        
        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=670,height=500)
        
        
        # img_left=Image.open(r"E:/Face Recognition/college_images/iStock-182059956_18390_t12.jpg")
        # img_left=img_left.resize((720,120),Image.LANCZOS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        # f_label=Label(Left_frame,image=self.photoimg_left)
        # f_label.place(x=5,y=0,width=620,height=120)
        
        #current course
        current_course=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("Times New Roman",12,"bold"))
        current_course.place(x=5,y=5,width=650,height=150)
        
        #Departments
        dep_label=Label(current_course,text="Departments:-",font=("Times New Roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("Times New Roman",12,"bold"),width=17,state="read only ")
        dep_combo["values"]=("Select Department","CSE","AI & DS","ENTC","ELECTRICAL","CIVIL","MECHANICAL","MECHATRONICS","AUTOMATION & ROBOTICS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course
        course_label=Label(current_course,text="Course:-",font=("times New Roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times New Roman",12,"bold"),width=20,state="read only ")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        year_label=Label(current_course,text="Year:-",font=("times New Roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("Times New Roman",12,"bold"),width=20,state="read only ")
        year_combo["values"]=("Select Year","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        semester_label=Label(current_course,text="Semester:-",font=("Times New Roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course,textvariable=self.var_semester,font=("Times New Roman",12,"bold"),width=20,state="read only ")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("Times New Roman",12,"bold"))
        class_student_frame.place(x=5,y=170,width=650,height=300)
        
        #Student ID
        studentId=Label(class_student_frame,text="studentId:",font=("Times New Roman",12,"bold"),bg="white")
        studentId.grid(row=0,column=0,padx=10,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_id,width=20,font=("Times New Roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Student Name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("Times New Roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_name,width=20,font=("Times New Roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Class Division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("Times New Roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("Times New Roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Times New Roman",12,"bold"),width=20,state="read only ")
        division_combo["values"]=("A","B")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("Times New Roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("Times New Roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("Times New Roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("Times New Roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Times New Roman",12,"bold"),width=20,state="read only ")
        gender_combo["values"]=("Male","female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Date of Birth
        dob_label=Label(class_student_frame,text="DOB:",font=("Times New Roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Times New Roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        email_label=Label(class_student_frame,text="E-mail:",font=("Times New Roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Times New Roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #Phone No
        phone_label=Label(class_student_frame,text="Phone No:",font=("Times New Roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Times New Roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        address_label=Label(class_student_frame,text="Address:",font=("Times New Roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Times New Roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("Times New Roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Times New Roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #button_frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)        
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)        
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)       
        
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=645,height=30) 
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=36,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=36,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        
        #Right frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Times New Roman",12,"bold"))
        Right_frame.place(x=680,y=10,width=630,height=500)
        
        img_right=Image.open(r"E:/Face Recognition/college_images/iStock-182059956_18390_t12.jpg")
        img_right=img_right.resize((610,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_label=Label(Right_frame,image=self.photoimg_right)
        f_label.place(x=5,y=0,width=610,height=130)
        
        #Search System
        
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Times New Roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=615,height=70)
        
        search_label=Label(Search_frame,text="Search By:",font=("Times New Roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=8,pady=4,sticky=W)
        
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=("Times New Roman",12,"bold"),width=15,state="readonly ")
        search_combo["values"]=("Select","Roll No","Phone","StudentId")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
       
        self.var_search=StringVar()
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=15,font=("Times New Roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=8,pady=4,sticky=W)
        
        search_btn=Button(Search_frame,command=self.search_data,text="Search",width=11,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)        
        
        showAll_btn=Button(Search_frame,command=self.fetch_data,text="Show All",width=11,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2)   
        
         
        #Table Frame
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=615,height=280)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","year","sem","id","name","div","roll","gender","phone","address","photo","teacher","course","email","dob"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Departments")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")        
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("email",text="E-mail")
        self.student_table.heading("dob",text="DOB")
        
        
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100) 
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)
        self.student_table.column("teacher",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       
# ----------Function----------------

    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',port='3306',username='root',password='',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              self.var_stu_id.get(),
                                                                                                              self.var_stu_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                              self.var_teacher.get(), 
                                                                                                              self.var_course.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_dob.get()    
                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been addes succcessfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)
                
                      
    #============fetch data=====    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',port='3306',username='root',password='',database='face_recognizer')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#===============get cursor=============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_stu_id.set(data[3]),
        self.var_stu_name.set(data[4]),
        self.var_div.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_address.set(data[9]),
        self.var_radio1.set(data[10]),
        self.var_teacher.set(data[11]), 
        self.var_course.set(data[12]),
        self.var_email.set(data[13]),
        self.var_dob.set(data[14]),   
                
    
#update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost',port='3306',username='root',password='',database='face_recognizer')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set department=%s,year=%s,sem=%s,student_name=%s,division=%s,roll_no =%s,gender=%s ,phone=%s,address=%s,photo=%s,teacher=%s,course =%s,email =%s,dob=%s where stu_id=%s",(self.var_dep.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              self.var_stu_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                              self.var_teacher.get(), 
                                                                                                              self.var_course.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_stu_id.get()
                                                                                                              ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Srudent details update successfully")
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)
    
    
    
    #=======delete function==================
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delte this student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',port='3306',username='root',password='',database='face_recognizer')
                    my_cursor=conn.cursor()
                    sql="delete from student where stu_id=%s"
                    val=(self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deteted student data")
                
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)    
                
    #============reset data================
    def reset_data(self):
        self.var_dep.set("Select Department") 
        self.var_course.set("Select course") 
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester") 
        self.var_stu_id.set("") 
        self.var_stu_name.set("") 
        self.var_div.set("A")        
        self.var_roll.set("") 
        self.var_gender.set("Male") 
        self.var_dob.set("") 
        self.var_email.set("") 
        self.var_phone.set("") 
        self.var_address.set("") 
        self.var_teacher.set("") 
        self.var_radio1.set("") 

#=============serach data======
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option ")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',port='3306',username='root',password='',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)
                
                
                
                
                
                
                
        
#===============gnerate data set==============

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',port='3306',username='root',password='',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set department=%s,year=%s,sem=%s,student_name=%s,division=%s,roll_no =%s,gender=%s ,phone=%s,address=%s,photo=%s,teacher=%s,course =%s,email =%s,dob=%s where stu_id=%s",(self.var_dep.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              self.var_stu_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                              self.var_teacher.get(), 
                                                                                                              self.var_course.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_stu_id.get()==id+1
                                                                                                              ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

#================Load predefined data on face frontals from opencv============

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor-1.3
                    #minimun neighbour=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed completed!")
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)  
                
                    
    
                
   
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
