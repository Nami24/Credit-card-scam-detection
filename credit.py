import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd

root = tk.Tk()
root.geometry("500x500")
root.pack_propagate(False)
root.resizable(0, 0)

frame1 = tk.LabelFrame(root, text="Excel data")
frame1.place(height=250, width=500)
 
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=400, rely=0.65, relx=0)

btn1 = tk.Button(file_frame, text="Brows a file",
                 command=lambda: file_dialog())
btn1.place(rely=0.65, relx=0.50)

btn2 = tk.Button(file_frame, text="Load file", command=lambda: load_data())
btn2.place(rely=0.65, relx=0.30)

label_file = ttk.Label(file_frame, text="No file selected")
label_file.place(rely=0, relx=0)

tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)

tree_scroll_y = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
tree_scroll_x = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=tree_scroll_x.set,
              yscrollcommand=tree_scroll_y.set)
tree_scroll_x.pack(side="bottom", fill="x")
tree_scroll_y.pack(side="right", fill="y")


def file_dialog():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a file", filetype=(("csv files", "*.csv"), ("All files", "*.*")))
    label_file["text"] = filename
    return None


def load_data():
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        df = pd.read_csv(excel_filename)
    except ValueError:
        tk.messagebox.showerror(
            "Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
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


root.mainloop()
