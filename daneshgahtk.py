from tkinter import *
from customtkinter import *
import mysql.connector as msc

root=Tk()
root.geometry("800x550")
root.title("log in")
root.resizable(False,False)
root.configure(background="#673dff")

'''
img=PhotoImage(file="word-image-5.png")
imglabel=Label(root,image=img,width=400,height=500,bg="#673dff")
imglabel.place(x=60,y=10)
'''

frame=CTkFrame(root,bg_color="#673dff",fg_color="#ffffff",width=310,height=400,corner_radius=20)
frame.place(x=460,y=70)

font=CTkFont(family="Helvetica",size=30,slant="italic")
label_name=CTkLabel(root,text="log in",font=font,bg_color="#ffffff")
label_name.place(x=575,y=100)

font2=CTkFont(family="Helvetica",size=18,slant="italic")
user_label=CTkLabel(root,text="user",font=font2,bg_color="#ffffff")
user_label.place(x=490,y=180)

user_entry=CTkEntry(root,placeholder_text="enter youe username...",width=200,corner_radius=15,bg_color="#ffffff")
user_entry.place(x=550,y=180)

pass_label=CTkLabel(root,text="pass",font=font2,bg_color="#ffffff")
pass_label.place(x=485,y=225)

pass_entry=CTkEntry(root,placeholder_text="enter youe password...",width=200,corner_radius=15,bg_color="#ffffff")
pass_entry.place(x=550,y=225)

btn_sign=CTkButton(root,text="sign in",text_color="#ffffff",width=240,bg_color="#ffffff",corner_radius=15,fg_color="#673dff",hover_color="#b38bff")
btn_sign.place(x=500,y=300)

label_logtext=CTkLabel(root,text="do you have an account? ",bg_color="#ffffff")
label_logtext.place(x=520,y=340)

btn_log=Button(root,text="log in ",fg="blue",bg="#ffffff",border=0)
btn_log.place(x=675,y=342)
'''
icon_img=PhotoImage(file="photo2.png")
root.iconphoto(True,icon_img)
'''


# Connect to the database
db = msc.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
cursor = db.cursor()

cursor.execute("create database if not exists python")
cursor.execute("create table if not exists users (id INT PRIMARY KEY AUTO_INCREMENT,user VARCHAR(20),pass VARCHAR(30));")
#
def login():
    user = user_entry.get()
    passw = pass_entry.get()
    cursor.execute("SELECT * FROM users WHERE user = %s AND pass = %s", (user, passw))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Invalid username or password")
        
btn_log.configure(command=login)
#
def sign_in():
    user = user_entry.get()
    passw = pass_entry.get()
    if user and passw:
        cursor.execute("SELECT * FROM users WHERE user = %s", (user,))
        if not cursor.fetchone():
            new_pass_label=CTkLabel(root,text="re-enter your password",font=font2,bg_color="#ffffff")
            new_pass_label.place(x=485,y=260)
            new_pass_entry=CTkEntry(root,placeholder_text="re-enter your password...",width=200,corner_radius=15,bg_color="#ffffff")
            new_pass_entry.place(x=550,y=260)
            def verify_password():
                re_entered_pass = new_pass_entry.get()
                if re_entered_pass == passw:
                    print("Password verified successfully!")
                    new_pass_label.destroy()
                    new_pass_entry.destroy()
                    cursor.execute("INSERT INTO users (user, pass) VALUES (%s, %s)", (user, passw))
                    db.commit()
                    print("User created successfully!")
                else:
                    print("Passwords do not match. Please try again.")
            btn_verify = CTkButton(root, text="Verify", command=verify_password,width=10)
            btn_verify.place(x=520, y=300)
            
        else:
            print("usr exist")
    else:
        print("Please enter your username and password.")

btn_sign.configure(command=sign_in)


root.mainloop()
