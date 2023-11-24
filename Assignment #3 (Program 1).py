import sqlite3
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from PIL import ImageTk, Image

# WINDOW CONFIGURATION
root = Tk()
root.title("PLD ASSIGNMENT 3 (PROGRAM 1)")
root.geometry("600x400")
image_0=Image.open("C:\\Users\\M2\\Desktop\\image.jpeg")
bck_end=ImageTk.PhotoImage(image_0)
lbl=Label(root,image=bck_end)
lbl.place(x=0,y=0)
root.resizable(False,False)

# FUNCTIONALITIES
   
apple_price = 20
orange_price = 25
total_price = 0
qty_apple = 0
qty_orange = 0

def pay():
    global total_price, qty_apple, qty_orange

    # Retrieve values from Entry widgets and convert to integers
    try:
        qty_apple = int(Entryapple.get())
        qty_orange = int(Entryorange.get())
    except ValueError:
        messagebox.showwarning(title="Error", message="Please enter valid numeric values.")
        return

    total_price = qty_apple * apple_price + qty_orange * orange_price

    if total_price == 0:
        messagebox.showwarning(title="Error", message="Please select at least one.")
    else:
        messagebox.showinfo(title="Successful Purchase", message="Your Total is ₱" + str(total_price))
    Entryname.delete(0, "end")
    Entryapple.delete(0, "end")
    Entryorange.delete(0, "end")




frame=Tk.frame

# LABELS
titleLabel = Label(root, text=("Aling Nena's Fruit Stall"), bg="#00A36C", fg="#E5E9EC", font=("Arial bold", 30),bd=2)
nameLabel=Label(root,text="Customer Name", bg="#00A36C", fg="#E5E9EC",font=("Arial bold", 15))
orangeLabel=Label(root,text="ORANGE [₱25/pc]", bg="#00A36C", fg="#E5E9EC", font=("Arial bold", 15))
appleLabel=Label(root,text="APPLE [₱20/pc]", bg="#00A36C", fg="#E5E9EC", font=("Arial bold", 15))

# LABEL POSITIONS
titleLabel.grid(row=0,column=0,columnspan=8,padx=20,pady=20)
nameLabel.grid(row=2,column=0,padx=10,pady=10)
orangeLabel.grid(row=3,column=0,padx=10,pady=10)
appleLabel.grid(row=4,column=0,padx=10,pady=10)

# ENTRIES

Entryname=Entry(root, width=25, bd=5, font=("Arial Bold 15",15))
Entryorange=Entry(root, width=25, bd=5, font=("Arial Bold 15",15))
Entryapple=Entry(root, width=25, bd=5, font=("Arial Bold 15",15))

# ENTRY POSITIONS

Entryname.grid(row=2,column=1,columnspan=3,padx=5,pady=5)
Entryorange.grid(row=3,column=1,columnspan=3,padx=5,pady=5)
Entryapple.grid(row=4,column=1,columnspan=3,padx=5,pady=5)

# Confirm Button
buttonEnter=Button(
    root, text="Purchase",padx=5,pady=5,width=7,bd=3,
    font=("Arial",15),bg="#00A36C",fg="#E5E9EC", command=pay
)
buttonEnter.grid(row=5,column=1,columnspan=1)

frame=Pack()

root.mainloop()
