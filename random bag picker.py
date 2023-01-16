from tkinter import *
root=Tk()
import random
root.title("List")
root.geometry("600x600")
label2=Label(root)
label=Label(root, text="Listed Items : ")
item=["Pen", "Tiffin", "Water Bottle", "Snacks", "Book", "Chocolate", "Hanky"]
def nextitem():
    label["text"] =  "Listed Items : " + str(item)
    rand=random.randint(1,7)
    label2["text"]="Put Item Number : " + str(rand)
btn=Button(root, text="Show Next Item", command=nextitem)
btn.configure(background="yellow")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label.place(relx=0.5, rely=0.3, anchor=CENTER)
label2.place(relx=0.5, rely=0.7, anchor=CENTER)
root.mainloop()