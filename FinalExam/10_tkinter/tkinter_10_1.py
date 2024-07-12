import tkinter

window=tkinter.Tk()
window.title("Simple GUI App")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0,row=0)
my_label.config(text="new label")

#Button
def button_clicked():
    new_text = my_input.get()
    my_label.config(text=new_text)

my_button = tkinter.Button(text="click me", command=button_clicked)
# my_button.pack()
my_button.grid(column=1,row=1)

#Entry
my_input = tkinter.Entry(width=20)
# my_input.pack()
my_input.grid(column=0,row=1)

window.mainloop()