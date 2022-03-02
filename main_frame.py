from ctypes import alignment
from distutils import command
from fileinput import filename
from msilib.schema import ListBox, RadioButton
from re import A
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter import font
from turtle import bgcolor, width
from PIL import ImageTk
from matplotlib import image
from matplotlib.pyplot import text
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd
import pymysql

root = Tk()
root.title("Credit Card Scame Detection System")
root.iconbitmap('images/img1.ico')
root.geometry("1350x690+0+0")
root.resizable(FALSE, FALSE)

# ---------------------------------- menubar ---------------------------------

menu_frame = Frame(root, bd=0, bg="#4056A1",
                   relief=RAISED,  width=1500, height=40)
menu_frame.pack(padx=0, pady=0)

label_frame = Label(
    menu_frame, text="CREDIT CARD SCAM DETECTION", font=("Helvetica", 15, "bold"), bg="#4056A1", fg="#EFE2BA")
label_frame.place(x=40, y=7)

# ------------------------------------ home frame ----------------------------------


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

    upload_btn = Button(home_frame, command=upload_window, text="Upload Files", bd=0, cursor="hand2", font=(
        "Helvetica", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA")
    upload_btn.place(x=600, y=250, height=35, width=140)

# ----------------------------- defining upload window --------------------------------

    # root1 = Toplevel()
    # root1.geometry("1300x700+0+0")
    # root1.pack_propagate(False)
    # root1.resizable(0, 0)
    # root1.config(bg="#C5CBE3")
    # root1.focus_force()
    # root1.grab_set()

    # frame1 = tk.LabelFrame(root1, text="Excel data", bg="#C5CBE3")
    # frame1.place(height=500, width=1300)

    # file_frame = tk.LabelFrame(root1, text="Open File")
    # file_frame.place(height=100, width=400, rely=0.75, relx=0.35)

    # btn1 = tk.Button(file_frame, text="Brows a file",
    #                  command=lambda: file_dialog())
    # btn1.place(rely=0.65, relx=0.50)

    # btn2 = tk.Button(file_frame, text="Load file", command=lambda: load_data())
    # btn2.place(rely=0.65, relx=0.30)

    # label_file = ttk.Label(file_frame, text="No file selected")
    # label_file.place(rely=0, relx=0)

    # tv1 = ttk.Treeview(frame1)
    # tv1.place(relheight=1, relwidth=1)

    # tree_scroll_y = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
    # tree_scroll_x = tk.Scrollbar(
    #     frame1, orient="horizontal", command=tv1.xview)
    # tv1.configure(xscrollcommand=tree_scroll_x.set,
    #               yscrollcommand=tree_scroll_y.set)
    # tree_scroll_x.pack(side="bottom", fill="x")
    # tree_scroll_y.pack(side="right", fill="y")

    # def file_dialog():
    #     filename = filedialog.askopenfilename(
    #         initialdir="/", title="Select a file", filetype=(("csv files", "*.csv"), ("All files", "*.*")))
    #     label_file["text"] = filename
    #     return None

    # def load_data():
    #     file_path = label_file["text"]
    #     try:
    #         excel_filename = r"{}".format(file_path)
    #         df = pd.read_csv(excel_filename)
    #     except ValueError:
    #         tk.messagebox.showerror(
    #             "Information", "The file you have chosen is invalid")
    #         return None
    #     except FileNotFoundError:
    #         tk.messagebox.showerror(
    #             "Information", f"No such file as {file_path}")
    #         return None

    #     clear_data()
    #     tv1["columns"] = list(df.columns)
    #     tv1["show"] = "headings"
    #     for column in tv1["columns"]:
    #         tv1.heading(column, text=column)

    #     df_rows = df.to_numpy().tolist()
    #     for row in df_rows:
    #         tv1.insert("", "end", values=row)
    #     return None

    # def clear_data():
    #     tv1.delete(*tv1.get_children())


# def upload_window():
#     upload_frame1 = Frame(root, width=1350, height=700,
#                           bg="#C5CBE3")
#     upload_frame1.place(x=0, y=40)

#     upload_frame2 = Frame(upload_frame1, width=650, height=400,
#                           bg="#EFE2BA")
#     upload_frame2.place(x=360, y=100)

#     title1 = Label(upload_frame2,  text="Upload Credit Card Dataset", font=(
#         "times new roman", 20, "bold"), bg="#D79922", fg="#4056A1")
#     title1.place(x=0, y=0, width=650)

#     filename = Label(upload_frame2,  text="File Name", font=(
#         "times new roman", 15, "bold"), bg="#EFE2BA", fg="black")
#     filename.place(x=40, y=50)
#     txt_file = ttk.Entry(upload_frame2, font=("times new roman", 15)
#                          )
#     txt_file.place(x=50, y=80, width=350)

#     def browse_fxn():
#         op = filedialog.askopenfile(title="Select File")
#         if op != None:
#             # print(op)
#             var_filename.set(str(op))

#     upload = Label(upload_frame2, text="Upload Credit Card Dataset File", font=(
#         "times new roman", 15, "bold"), bg="#EFE2BA", fg="black")
#     upload.place(x=40, y=120)

#     choose = Button(upload_frame2, bd=0, bg="gray", cursor="hand2", command=browse_fxn, activebackground="black", activeforeground="White", text="Choose File", font=("times new roman", 13)
#                     )
#     choose.place(x=50, y=150, width=100)

#     var_filename = StringVar()
#     txt_choosefile = ttk.Entry(upload_frame2, textvariable=var_filename, font=(
#         "times new roman", 15, "bold"))
#     txt_choosefile.place(x=150, y=150, width=250)

#     desc = Label(upload_frame2, text="Description of File", font=(
#         "times new roman", 15, "bold"), bg="#EFE2BA", fg="black")
#     desc.place(x=40, y=190)
#     txt_desc = Text(upload_frame2, font=("times new roman", 15), bg="white", height=6,
#                     width=35
#                     )
#     txt_desc.place(x=50, y=220)

#     submit_btn = Button(upload_frame2, text="Submit", bd=0, cursor="hand2", font=(
#         "arial", 16, "bold"), bg="black", fg="white", activebackground="black", activeforeground="White")
#     submit_btn.place(x=500, y=320, height=35, width=100)


def upload_window():
    upload_frame1 = Frame(root, width=1350, height=700,
                          bg="#C5CBE3")
    upload_frame1.place(x=0, y=40)
    frame1 = tk.LabelFrame(upload_frame1, width=1040, height=640, text="Credit Card Data Set",
                           bg="#C5CBE3")
    frame1.place(x=300, y=5)

    file_frame = tk.LabelFrame(upload_frame1, text="Open File", bg="#C5CBE3")
    file_frame.place(height=640, width=280, x=10, y=5)

    btn1 = tk.Button(file_frame, text="Browse a file", cursor="hand2", bd=0, font=("times new roman", 15),
                     command=lambda: file_dialog())
    btn1.place(relx=0.06, rely=0.10, width=240, height=30)

    btn2 = tk.Button(file_frame, text="View Data",
                     command=lambda: view_data(), cursor="hand2", bd=0, font=("times new roman", 15))
    btn2.place(relx=0.06, rely=0.30,  width=240, height=30)

    btn3 = tk.Button(file_frame, text="Prediction", cursor="hand2",
                     bd=0, font=("times new roman", 15))
    btn3.place(relx=0.06, rely=0.40, width=240, height=30)

    btn4 = tk.Button(file_frame, text="Analysis", bd=0, cursor="hand2",
                     font=("times new roman", 15))
    btn4.place(relx=0.06, rely=0.50, width=240, height=30)

    btn5 = tk.Button(file_frame, text="Clear Data", bd=0,  cursor="hand2",
                     font=("times new roman", 15))
    btn5.place(relx=0.06, rely=0.60, width=240, height=30)

    label_file = ttk.Label(file_frame, text="No file selected")
    label_file.place(relx=0.05, rely=0.01)

    tv1 = ttk.Treeview(frame1)
    tv1.place(height=620, width=1035)

    tree_scroll_y = tk.Scrollbar(tv1, orient="vertical", command=tv1.yview)
    tree_scroll_x = tk.Scrollbar(
        tv1, orient="horizontal", command=tv1.xview)
    tv1.configure(xscrollcommand=tree_scroll_x.set,
                  yscrollcommand=tree_scroll_y.set)
    tree_scroll_x.pack(side="bottom", fill="x")
    tree_scroll_y.pack(side="right", fill="y")

    def file_dialog():
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select a file", filetype=(("csv files", "*.csv"), ("All files", "*.*")))
        label_file["text"] = filename
        return None

    def view_data():
        file_path = label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            df = pd.read_csv(excel_filename)
        except ValueError:
            tk.messagebox.showerror(
                "Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror(
                "Information", f"No such file as {file_path}")
            return None

        clear_data()
        tv1["columns"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tv1.insert("", "end", values=row)
        return None

    def clear_data():
        tv1.delete(*tv1.get_children())


home = Button(menu_frame, text="Home", command=Home, bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=640, y=6, height=35, width=50)

# --------------------------------about frame ------------------------------


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


About = Button(menu_frame, text="About", command=About, bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=710, y=6, height=35, width=50)

#  -------------------------------- administration frame ------------------------

admin = Button(menu_frame, text="Administration", bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=780, y=6, height=35, width=110)

# --------------------------------- report frame -----------------------

report = Button(menu_frame, text="Report", bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=910, y=6, height=35, width=60)

# ------------------------------------- acc frame -----------------------


def Account():
    account_frame = Frame(root, width=1350, height=700, bg="#C5CBE3")
    account_frame.place(x=0, y=40)

    acc_frame = Frame(account_frame, height=1000, width=800, bg="#EFE2BA")
    acc_frame.place(x=300, y=50)

    title1 = Label(acc_frame,  text="My Profile", font=(
        "times new roman", 20, "bold"), bg="#D79922", fg="#4056A1")
    title1.place(x=0, y=0, width=800)

    title2 = Label(acc_frame,  text="User Login Details", font=(
        "times new roman", 14), bg="#EFE2BA", fg="black")
    title2.place(x=30, y=60)

    hr = Label(acc_frame, bg="black")
    hr.place(x=30, y=85, height=2, width=750)

    # --------------- row1 --------------------------

    fn = Label(acc_frame, text="User First Name", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    fn.place(x=40, y=110)

    txt_fn = ttk.Entry(acc_frame, font=("arial", 13)
                       )
    txt_fn.place(x=40, y=140, width=350)

    ln = Label(acc_frame, text="User Last Name", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    ln.place(x=420, y=110)

    txt_ln = ttk.Entry(acc_frame, font=("arial", 13)
                       )
    txt_ln.place(x=420, y=140, width=350)

    # ------------------------- row2 -----------------

    contact = Label(acc_frame, text="Contact No.", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    contact.place(x=40, y=190)
    txt_contact = ttk.Entry(acc_frame, font=("arial", 13),
                            )
    txt_contact.place(x=40, y=220, width=350)

    email = Label(acc_frame, text="Email", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    email.place(x=420, y=190)
    txt_email = ttk.Entry(acc_frame, font=("arial", 13),
                          )
    txt_email.place(x=420, y=220, width=350)

    # ------------------------ row3 ----------------------

    title2 = Label(acc_frame,  text="User Personal Details", font=(
        "times new roman", 14), bg="#EFE2BA", fg="black")
    title2.place(x=30, y=265)

    hr = Label(acc_frame, bg="black")
    hr.place(x=30, y=290, height=2, width=750)

    # ---------------------- row4 -----------------------------

    gender = Label(acc_frame, text="Gender", font=(
        "arial", 13), bg="#EFE2BA", fg="black")
    gender.place(x=40, y=300)
    gender_btn = RadioButton(acc_frame, text="")

    # pswd = Label(acc_frame, text="Password", font=(
    #     "arial", 13), bg="#EFE2BA", fg="black")
    # pswd.place(x=40, y=330)
    # txt_pswd = ttk.Entry(acc_frame, font=("arial", 13),
    #                      )
    # txt_pswd.place(x=40, y=360, width=250)

    # cpswd = Label(acc_frame, text="Confirm Password", font=(
    #     "arial", 13), bg="#EFE2BA", fg="black")
    # cpswd.place(x=320, y=330)
    # txt_cpswd = ttk.Entry(acc_frame, font=("arial", 13),
    #                       )
    # txt_cpswd.place(x=320, y=360, width=250)


my_acc = Button(menu_frame, text="My Account", bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), command=Account, bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=990, y=6, height=35, width=90)

# ---------------------------------logout frame --------------------------

logout = Button(menu_frame, text="Logout", bd=0, cursor="hand2", font=(
    "arial", 11, "bold"), bg="#4056A1", fg="#EFE2BA", activebackground="#4056A1", activeforeground="#EFE2BA").place(x=1100, y=6, height=35, width=60)


root.configure(Home())
root.mainloop()
