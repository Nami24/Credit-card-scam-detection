from fileinput import filename
from re import search
from tkinter import*
from tkinter import ttk, messagebox, filedialog
from tkinter import font
from turtle import width
from PIL import Image, ImageTk
from matplotlib.pyplot import table


class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("CREDIT CARD SCAM DETECTION")
        root.iconbitmap('images/img1.ico')
        self.root.geometry("1350x700+0+0")
        # bg image
        self.bg = ImageTk.PhotoImage(file="images/bgimg.jpg")
        bg = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # main frame

        frame3 = Frame(self.root, bg="white")
        frame3.place(x=250, y=120, width=900, height=500)

        title = Label(frame3, text="DASHBOARD", font=(
            "times new roman", 20, "bold"), bg="black", fg="#e5b73b").place(x=50, y=30, width=800, height=40)

        # buttons

        btn_1 = Button(frame3, text="Report Files", bd=0, activebackground="#e5b73b", activeforeground="White", command=self.upload_window, cursor="hand2", font=(
            "arial", 16, "bold"), bg="#e5b73b", fg="white").place(x=200, y=130, height=80, width=200)

        btn_2 = Button(frame3, text="My Account", bd=0, activebackground="#e5b73b", activeforeground="White", cursor="hand2", font=(
            "arial", 16, "bold"), bg="#e5b73b", fg="white").place(x=500, y=130, height=80, width=200)

        self.logout_btn = ImageTk.PhotoImage(file="images/logout.png")
        btn_3 = Button(frame3, image=self.logout_btn, bd=0, cursor="hand2").place(
            x=840, y=440)

     # ======= Report files ============

    def upload_window(self):
        self.root3 = Toplevel()
        self.root3.title("UPLOAD FILES")
        root.iconbitmap('images/img1.ico')
        self.root3.geometry("1350x700+0+0")
        self.root3.config(bg="#e5b73b")
        self.root3.focus_force()
        self.root3.grab_set()

        frame_1 = Frame(self.root3, bd=4, relief=RIDGE, bg="lightgray")
        frame_1.place(x=20, y=10, width=1310, height=300)

        title_1 = Label(frame_1, text="Upload Credit Card Dataset", font=(
            "times new roman", 20, "bold"), bg="black", fg="white")
        title_1.place(x=0, y=10, relwidth=1)

        # filename = Label(self.root3,  text="File Name", font=(
        #     "times new roman", 15, "bold"), bg="white", fg="black").place(x=40, y=70)
        # self.txt_file = ttk.Entry(self.root3, font=("times new roman", 15),
        #                           )
        # self.txt_file.place(x=50, y=100, width=350)

        # upload = Label(self.root3, text="Upload Credit Card Dataset File", font=(
        #     "times new roman", 15, "bold"), bg="white", fg="black").place(x=40, y=150)
        # self.choose = Button(self.root3, bd=0, bg="gray", cursor="hand2", command=self.browse_fxn, activebackground="black", activeforeground="White", text="Choose File", font=("times new roman", 13)
        #                      )
        # self.choose.place(x=50, y=190, width=100)

        # self.var_filename = StringVar()

        # txt_choosefile = ttk.Entry(self.root3, textvariable=(self.var_filename, self.original_variable), font=(
        #     "times new roman", 15, "bold")).place(x=150, y=190, width=250)

        # desc = Label(self.root3, text="Description of File", font=(
        #     "times new roman", 15, "bold"), bg="white", fg="black").place(x=540, y=70)
        # self.txt_desc = Text(self.root3, font=("times new roman", 15), bg="white", height=6,
        #                      width=40
        #                      )
        # self.txt_desc.place(x=550, y=100)

        # submit_btn = Button(self.root3, text="Submit", bd=0, cursor="hand2", font=(
        #     "arial", 16, "bold"), bg="black", fg="white", activebackground="black", activeforeground="White").place(x=1200, y=200, height=35, width=100)

        # # ==========report frame=============

        frame_2 = Frame(self.root3, bg="lightgray", bd=4, relief=RIDGE)
        frame_2.place(x=20, y=320, width=1310, height=370)

        title_2 = Label(frame_2, text="All Credit Card Dataset", font=(
            "times new roman", 20, "bold"), bg="black", fg="white").place(x=0, y=20, relwidth=1)

        # searchby = Label(report_frame, text="Search By", bg="lightgray", fg="black",
        #                  font=("times new roman", 15, "bold"))
        # searchby.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # combo_search = ttk.Combobox(report_frame, font=(
        #     "times new roman", 13, "bold"), width=15, state='readonly')
        # combo_search['value'] = ("srno.", "file name", "original file name")
        # combo_search.grid(row=0, column=1, pady=10,
        #                   padx=20)

        # txt_search = ttk.Entry(report_frame,  font=(
        #     "times new roman", 13, "bold"))
        # txt_search.grid(row=0, column=2, pady=10,
        #                 padx=20, sticky="w")

        # search_btn = Button(report_frame, text="Search",  font=(
        #     "times new roman", 13, "bold"), width=10, bd=0, cursor="hand2", bg="#e5b73b").grid(row=0, column=3, pady=10,
        #                                                                                        padx=10)
        # show_btn = Button(report_frame, text="Show All",  font=(
        #     "times new roman", 13, "bold"), width=10, bd=0, cursor="hand2",  bg="#e5b73b").grid(row=0, column=4, pady=10,
        #                                                                                         padx=10)

        # # ========== table frame ==========

        # table_frame = Frame(report_frame, relief=RIDGE, bg="lightgray", bd=4)
        # table_frame.place(x=10, y=50, height=290, width=1300)

        # scrollx = Scrollbar(table_frame, orient=HORIZONTAL)
        # scrolly = Scrollbar(table_frame, orient=VERTICAL)
        # table = ttk.Treeview(table_frame,  columns=(
        #     "srno", "file name", "original file name", "action"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        # scrollx.pack(side=BOTTOM, fill=X)
        # scrolly.pack(side=RIGHT, fill=Y)
        # scrollx.config(command=table.xview)
        # scrolly.config(command=table.yview)
        # table.heading("srno", text="Sr.No.")
        # table.heading("file name", text="File Name")
        # table.heading("original file name", text="Original File Name")
        # table.heading("action", text="Action")
        # table['show'] = 'headings'
        # table.column("srno", width=100)
        # table.column("file name", width=230)
        # table.column("original file name", width=230)
        # table.column("action", width=390)
        # table.pack(fill=BOTH, expand=1)

        # view = Button(self.root4, text="View Details", bd=0, cursor="hand2", font=(
        #     "arial", 12, "bold"), bg="green", fg="white").place(x=40, y=60, height=35, width=100)

        # delete = Button(self.root4, text="Delete", bd=0, cursor="hand2", font=(
        #     "arial", 12, "bold"), bg="red", fg="white").place(x=150, y=60, height=35, width=80)

        # predict = Button(self.root4, text="Prediction", bd=0, cursor="hand2", font=(
        #     "arial", 12, "bold"), bg="blue", fg="white").place(x=240, y=60, height=35, width=100)

        # Analysis = Button(self.root4, text="analysis", bd=0, cursor="hand2", font=(
        #     "arial", 12, "bold"), bg="blue", fg="white").place(x=350, y=60, height=35, width=100)

    # def browse_fxn(self):
    #     op = filedialog.askopenfile(title="Select File")
    #     if op != None:
    #         # print(op)
    #         self.var_filename.set(str(op))


root = Tk()
obj = MainPage(root)
root.mainloop()
