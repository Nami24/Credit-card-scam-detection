  upload_frame1 = Frame(root, width=1350, height=700,
                          bg="#C5CBE3")
    upload_frame1.place(x=0, y=40)

    upload_frame2 = Frame(upload_frame1, width=650, height=400,
                          bg="#EFE2BA")
    upload_frame2.place(x=360, y=100)

    title1 = Label(upload_frame2,  text="Upload Credit Card Dataset", font=(
        "times new roman", 20, "bold"), bg="#D79922", fg="#4056A1")
    title1.place(x=0, y=0, width=650)

    filename = Label(upload_frame2,  text="File Name", font=(
        "times new roman", 15, "bold"), bg="#EFE2BA", fg="black")
    filename.place(x=40, y=50)
    txt_file = ttk.Entry(upload_frame2, font=("times new roman", 15)
                         )
    txt_file.place(x=50, y=80, width=350)

    def browse_fxn():
        op = filedialog.askopenfile(title="Select File")
        if op != None:
            # print(op)
            var_filename.set(str(op))

    upload = Label(upload_frame2, text="Upload Credit Card Dataset File", font=(
        "times new roman", 15, "bold"), bg="#EFE2BA", fg="black")
    upload.place(x=40, y=120)

    choose = Button(upload_frame2, bd=0, bg="gray", cursor="hand2", command=browse_fxn, activebackground="black", activeforeground="White", text="Choose File", font=("times new roman", 13)
                    )
    choose.place(x=50, y=150, width=100)

    var_filename = StringVar()
    txt_choosefile = ttk.Entry(upload_frame2, textvariable=var_filename, font=(
        "times new roman", 15, "bold"))
    txt_choosefile.place(x=150, y=150, width=250)

    desc = Label(upload_frame2, text="Description of File", font=(
        "times new roman", 15, "bold"), bg="#EFE2BA", fg="black")
    desc.place(x=40, y=190)
    txt_desc = Text(upload_frame2, font=("times new roman", 15), bg="white", height=6,
                    width=35
                    )
    txt_desc.place(x=50, y=220)

    submit_btn = Button(upload_frame2, text="Submit", bd=0, cursor="hand2", font=(
        "arial", 16, "bold"), bg="black", fg="white", activebackground="black", activeforeground="White")
    submit_btn.place(x=500, y=320, height=35, width=100)