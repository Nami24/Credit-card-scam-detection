from ctypes import alignment
from distutils import command
from msilib.schema import ListBox
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk
from matplotlib.pyplot import text
import pymysql


root = Tk()
root.title("Credit Card Scame Detection System")
root.iconbitmap('images/img1.ico')
root.geometry("1350x700+0+0")
root.resizable(FALSE, FALSE)

#  ------------------------------ menubar -------------------------------

menu_frame = Frame(root, bd=0, bg="#4056A1",
                   relief=RAISED,  width=1500, height=40)
menu_frame.pack(padx=0, pady=0)

label_frame = Label(
    menu_frame, text="CREDIT CARD SCAM DETECTION", font=("Helvetica", 15, "bold"), bg="#4056A1", fg="#EFE2BA")
label_frame.place(x=40, y=7)

# ----------------------------- home frame -----------------------------------


def Home():
    home_frame = Frame(root, width=1350, height=700,
                       bg="#C5CBE3")
    home_frame.place(x=0, y=40)

    home_lbl1 = Label(
        home_frame, text=" Welcome to Credit Card Scam Detection System", bg="#C5CBE3", fg="#D79922", font=("times new roman", 30, "bold"))
    home_lbl1.place(x=230, y=160)

    home_lbl2 = Label(
        home_frame, text=" Complete Solution for Credit Card Scam Detection", bg="#C5CBE3", fg="#D79922", font=("times new roman", 15, "bold"))
    home_lbl2.place(x=460, y=210)

    register_btn = Button(home_frame, command=register_window, text="Register Now", bd=0, cursor="hand2", font=(
        "Helvetica", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA")
    register_btn.place(x=600, y=250, height=35, width=140)


home = Button(menu_frame, text="Home", command=Home, bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=860, y=6, height=35, width=50)

# ----------------------------------- about frame ------------------------------------------


def About():
    about_frame = Frame(root, width=1300, height=600, bg="#C5CBE3")
    about_frame.place(x=0, y=40)

    about_lbl1 = Label(about_frame, text="About - Credit Card Scam Detection",
                       font=("times new roman", 20, "bold"), bg="#C5CBE3", fg="#4056A1", anchor="w", justify=LEFT)
    about_lbl1.place(x=50, y=10)

    hr = Label(about_frame, bg="#4056A1")
    hr.place(x=40, y=50, height=2, width=1200)

    about_lbl2 = Label(about_frame, text="The challenge is to recognize fraudulent credit card transactions so that the customer of credit card companies are  not charged for\nitem they did not purchase.",
                       font=("Helvetica", 15), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl2.place(x=50, y=60)

    hr = Label(about_frame, bg="#4056A1")
    hr.place(x=40, y=120, height=2, width=1200)

    about_lbl3 = Label(about_frame, text="Main challenges involved in Credit Card Scam Detection are:",
                       font=("Helvetica", 18), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl3.place(x=50, y=140)

    about_lbl3_1 = Label(about_frame, text="• Enormous data is processed every day and the model build must be enough to respond to the scam in time.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl3_1.place(x=60, y=180)

    about_lbl3_2 = Label(about_frame, text="• Imbalanced data i.e. most of the transacction (99.8%) are not fraudulent which makes it really hard for detecting the fraudulent ones.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl3_2.place(x=60, y=205)

    about_lbl3_3 = Label(about_frame, text="• Data availbilty as the data is mostly private.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl3_3.place(x=60, y=230)

    about_lbl3_4 = Label(about_frame, text="• Misclassified data can be another major issue, as not every fraudulent transaction is caught and reported.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl3_4.place(x=60, y=255)
    about_lbl3_5 = Label(about_frame, text="• Adaptive techniquesused against the model by the scammers.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl3_5.place(x=60, y=280)

    about_lbl4 = Label(about_frame, text="How to tackle these challenges?",
                       font=("Helvetica", 18), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl4.place(x=50, y=320)

    about_lbl4_1 = Label(about_frame, text="• The model must used be simple and fast enough to detect and classify it as a fraudulent transaction as quickly as possible.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl4_1.place(x=60, y=360)

    about_lbl4_2 = Label(about_frame, text="• Imbalance can be dealt with by properly using some methods which will talk about in the next paragraph.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl4_2.place(x=60, y=385)

    about_lbl4_3 = Label(about_frame, text="• For protecting the privacy of the user the dimensionally of the data can be reduced.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl4_3.place(x=60, y=410)

    about_lbl4_4 = Label(about_frame, text="• A more trustworthy source must be taken which double-check the data, at least for training the model.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl4_4.place(x=60, y=435)

    about_lbl4_5 = Label(about_frame, text="• We can make the model simple and interpretable so that when the scammer adapts to it with just some tweaks wa can have a new model up and running to deploy.",
                         font=("Helvetica", 12), bg="#C5CBE3", fg="black", anchor="w", justify=LEFT)
    about_lbl4_5.place(x=60, y=460)


about = Button(menu_frame, text="About", command=About, bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=930, y=6, height=35, width=50)


# --------------------- login frame ----------------------------

def Login():
    login_frame = Frame(root, width=1300, height=600, bg="#C5CBE3")
    login_frame.place(x=0, y=40)

    login_lbl1 = Label(login_frame, text="Login to your Account",
                       font=("times new roman", 20, "bold"), bg="#C5CBE3", fg="#4056A1", anchor="w", justify=LEFT)
    login_lbl1.place(x=50, y=20)

    login_page = Frame(login_frame, bg="#EFE2BA")
    login_page.place(x=490, y=100, width=390, height=320)

    login_title1 = Label(login_page, text="Welcome back to our application", font=(
        "arial", 15, "bold"), bg="#EFE2BA", fg="#D79922")
    login_title1.place(x=40, y=20)

    login_title2 = Label(login_page, text="Do you have an account?",
                         font=("arial", 11), bg="#EFE2BA", fg="#D79922", anchor="w", justify=LEFT)
    login_title2.place(x=40, y=50)

    signup_btn = Button(login_page, text="Sign Up", command=register_window, bg="#EFE2BA", fg="#4065A1", activebackground="#EFE2BA", activeforeground="#4065A1",
                        cursor="hand2", bd=0, font=("times new roman", 11))
    signup_btn.place(
        x=210, y=50)

    email = Label(login_page, text="Email", font=(
        "arial", 13, "bold"), bg="#EFE2BA", fg="black")
    email.place(x=50, y=80)
    txt_email = ttk.Entry(login_page, font=("arial", 13),
                          )
    txt_email.place(x=60, y=110, width=250)

    password = Label(login_page, text="Password", font=(
        "arial", 13, "bold"), bg="#EFE2BA", fg="black")
    password.place(x=50, y=150)
    txt_pass = ttk.Entry(login_page, font=("arial", 13),
                         )
    txt_pass.place(x=60, y=180, width=250)

    #   -------------------- defining the login function ------------------------

    def login_data():
        if txt_email.get == "" or txt_pass.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=root)
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="manager")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",
                            (txt_email.get(), txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Username & Password", parent=root)
                else:
                    messagebox.showinfo(
                        "Success", "Welcome", parent=root)
                    root.destroy()
                    import main
                    con.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=root)

    login = Button(login_page, text="Login", command=login_data, bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA",
                   cursor="hand2", bd=0, font=("times new roman", 15, "bold"))
    login.place(x=50, y=260, width=265, height=30)

    # ------------------ defining forget password -------------------------------

    def forget_password():
        if txt_email.get() == "":
            messagebox.showerror(
                "Error", "Please enter the valid email address to reset your password", parent=root)
        else:
            root2 = Toplevel()
            root2.title("Forget Password")
            root2.iconbitmap('images/img1.ico')
            root2.geometry("350x400+495+150")
            root2.config(bg="#C5CBE3")
            root2.resizable(FALSE, FALSE)
            root2.focus_force()
            root2.grab_set()

            txt = Label(root2, text="Forget Password", font=(
                "times new roman", 20, "bold"), bg="#C5CBE3", fg="#4056A1").place(x=0, y=10, relwidth=1)

            ques = Label(root2, text="Security Question", font=(
                "times new roman", 15, "bold"), bg="#C5CBE3", fg="black").place(x=40, y=100)
            combo_ques = ttk.Combobox(root2, font=("times new roman", 13), state="readonly"
                                      )
            combo_ques['values'] = ("select", "Your birth place?", "Your first pet name?",
                                    "Your favourite teacher name?", "Your best friend name?")
            combo_ques.place(x=50, y=130, width=250)
            combo_ques.current(0)

            ans = Label(root2, text="Answer", font=(
                "times new roman", 15, "bold"), bg="#C5CBE3", fg="black").place(x=40, y=180)
            txt_ans = ttk.Entry(root2, font=("times new roman", 15),
                                )
            txt_ans.place(x=50, y=210, width=250)

            password = Label(root2, text="New Password", font=(
                "times new roman", 15, "bold"), bg="#C5CBE3", fg="black").place(x=40, y=260)
            txt_pass = ttk.Entry(root2, font=("times new roman", 15),
                                 )
            txt_pass.place(x=50, y=290, width=250)

            btn_change = Button(root2, text="Change Password", bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA", cursor="hand2", bd=0, font=("times new roman", 15, "bold")).place(
                x=90, y=340, width=170, height=30)

    forget = Button(login_page, text="Forget Password?", command=forget_password, bd=0, font=(
        "arial", 11, "bold"), bg="#EFE2BA", fg="#D79922", activebackground="#EFE2BA", activeforeground="#D79922")
    forget.place(x=50, y=210)


login = Button(menu_frame, text="Login", command=Login, bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=1000, y=6, height=35, width=50)

# ---------------------------------- contact frame --------------------------------------


def Contact():
    contact_frame = Frame(root, width=1300, height=600, bg="#C5CBE3")
    contact_frame.place(x=0, y=40)

    contact_lbl1 = Label(contact_frame, text="Contact Us",
                         font=("times new roman", 20, "bold"), bg="#C5CBE3", fg="#4056A1", anchor="w", justify=LEFT)
    contact_lbl1.place(x=50, y=20)

    contact_lbl2 = Label(contact_frame, text="Drop your massage so that we can contact you!", font=(
        "times new roman", 15), bg="#C5CBE3", fg="#4056A1", anchor="w", justify=LEFT).place(x=60, y=70)

    name = Label(contact_frame, text="Name", font=(
        "arial", 13, "bold"), bg="#C5CBE3", fg="black")
    name.place(x=60, y=120)
    txt_name = ttk.Entry(contact_frame, font=("arial", 13),
                         )
    txt_name.place(x=60, y=150, width=500)

    emails = Label(contact_frame, text="Email", font=(
        "arial", 13, "bold"), bg="#C5CBE3", fg="black")
    emails.place(x=60, y=180)
    txt_emails = ttk.Entry(contact_frame, font=("arial", 13),
                           )
    txt_emails.place(x=60, y=210, width=500)

    contact = Label(contact_frame, text="Phone", font=(
        "arial", 13, "bold"), bg="#C5CBE3", fg="black")
    contact.place(x=60, y=240)
    txt_cont = ttk.Entry(contact_frame, font=("arial", 13),
                         )
    txt_cont.place(x=60, y=270, width=500)

    msg = Label(contact_frame, text="Message", font=(
        "arial", 13, "bold"), bg="#C5CBE3", fg="black")
    msg.place(x=60, y=300)

    txt_msg = Text(contact_frame, font=("times new roman", 15), bg="white", bd=0,
                   )
    txt_msg.place(x=60, y=330, width=500, height=100)

    submit_btn = Button(contact_frame, font=(
        "arial", 11, "bold"), text="Submit", bg="#4056A1", fg="#EFE2BA", bd=0, activebackground="#4056A1", activeforeground="#EFE2BA").place(x=70, y=450, height=35, width=90)


contact = Button(menu_frame, text="Contact Us", command=Contact, bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=1070, y=6, height=35, width=90)

# ----------------------- register frame ------------------------------


def register_window():
    root1 = Toplevel()
    root1.iconbitmap('images/img1.ico')
    root1.title("Registration Page")
    root1.geometry("900x500+250+100")
    root1.config(bg="#EFE2BA")
    root1.resizable(FALSE, FALSE)
    root1.focus_force()
    root1.grab_set()

    title1 = Label(root1, text="Welcome to our application", font=(
        "arial", 20, "bold"), bg="#EFE2BA", fg="#D79922")
    title1.place(x=40, y=10)

    title2 = Label(root1, text="Let's set your account.", font=(
        "arial", 12), bg="#EFE2BA", fg="#D79922")
    title2.place(x=40, y=45)

    title3 = Label(root1, text="Already have an account?", font=(
        "arial", 11), bg="#EFE2BA", fg="#D79922")
    title3.place(x=40, y=80)

    def register_data():
        root1.destroy()
        Login()

    signin_btn = Button(root1, text="Sign In", command=register_data, bg="#EFE2BA", fg="#4056A1", activebackground="#EFE2BA", activeforeground="#4056A1",
                        cursor="hand2", bd=0, font=("times new roman", 11))
    signin_btn.place(
        x=210, y=80)

    # ------------------------- defining the registration function ---------------------------

    def register_fxn():
        if txt_fn.get() == "" or txt_ln.get() == "" or txt_contact.get() == "" or txt_email.get() == "" or combo_ques.get() == "Select" or txt_ans.get() == "" or txt_pswd.get() == "" or txt_cpswd.get() == "":
            messagebox.showerror(
                "Error", "All Fieds Are Required", parent=root1)
        elif txt_pswd.get() != txt_cpswd.get():
            messagebox.showerror(
                "Error", "Password & confirm password should be same", parent=root1)
        elif var_chk.get() == 0:
            messagebox.showerror(
                "Error", "Please Agree our Terms & Condition", parent=root1)
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="manager")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s",
                            txt_email.get())
                row = cur.fetchone()
                print(row)
                if row != None:
                    messagebox.showerror(
                        "Error", "User already Exist, Please tyr with another email", parent=root1)
                else:
                    cur.execute("insert into employee(fname,lname,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    txt_fn.get(),
                                    txt_ln.get(),
                                    txt_contact.get(),
                                    txt_email.get(),
                                    combo_ques.get(),
                                    txt_ans.get(),
                                    txt_pswd.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Register successful", parent=root1)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=root1)

    # --------------- row1 --------------------------

    fn = Label(root1, text="First Name", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    fn.place(x=40, y=120)

    txt_fn = ttk.Entry(root1, font=("arial", 13)
                       )
    txt_fn.place(x=40, y=150, width=250)

    ln = Label(root1, text="Last Name", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    ln.place(x=320, y=120)

    txt_ln = ttk.Entry(root1, font=("arial", 13)
                       )
    txt_ln.place(x=320, y=150, width=250)

    # ------------------------- row2 -----------------

    contact = Label(root1, text="Contact No.", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    contact.place(x=40, y=190)
    txt_contact = ttk.Entry(root1, font=("arial", 13),
                            )
    txt_contact.place(x=40, y=220, width=250)

    email = Label(root1, text="Email", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    email.place(x=320, y=190)
    txt_email = ttk.Entry(root1, font=("arial", 13),
                          )
    txt_email.place(x=320, y=220, width=250)

    # ------------------------ row3 ----------------------

    ques = Label(root1, text="Security Question", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    ques.place(x=40, y=260)
    combo_ques = ttk.Combobox(root1, font=("arial", 13), state="readonly"
                              )
    combo_ques['values'] = ("select", "Your birth place?", "Your first pet name?",
                            "Your favourite teacher name?", "Your best friend name?")
    combo_ques.place(x=40, y=290, width=250)
    combo_ques.current(0)

    ans = Label(root1, text="Answer", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    ans.place(x=320, y=260)
    txt_ans = ttk.Entry(root1, font=("arial", 13),
                        )
    txt_ans.place(x=320, y=290, width=250)

    # -------------------- row4 ------------------------

    pswd = Label(root1, text="Password", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    pswd.place(x=40, y=330)
    txt_pswd = ttk.Entry(root1, font=("arial", 13),
                         )
    txt_pswd.place(x=40, y=360, width=250)

    cpswd = Label(root1, text="Confirm Password", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    cpswd.place(x=320, y=330)
    txt_cpswd = ttk.Entry(root1, font=("arial", 13),
                          )
    txt_cpswd.place(x=320, y=360, width=250)

    # ------------------------ row5 ----------------------

    var_chk = IntVar()
    chk = Checkbutton(
        root1, text="I Agree The Terms & Condition", variable=var_chk, onvalue=1, offvalue=0, bg="#EFE2BA", fg="black", activebackground="#EFE2BA", activeforeground="black", font=("arial", 12))
    chk.place(x=50, y=400)

    # ------------------------------- row6 --------------------------

    btn = Button(root1, text="Register Now", command=register_fxn, bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA",
                 cursor="hand2", bd=0, font=("Helvetica", 14, "bold"))
    btn.place(
        x=40, y=440, width=530, height=30)

    register_image = ImageTk.PhotoImage(
        file="images/Rect.png")
    register_img = Label(root1, image=register_image)
    register_img.place(
        x=600, y=100)


root.configure(Home())
root. mainloop()
