import tkinter

window = tkinter.Tk()
window.title("Simple GUI App")
window.minsize(width=500,height=300)


#Label
my_label=tkinter.Label(
    text="first label",
    font=("Arial",24, "bold")
)
my_label.grid(column=0, row=0)

def button_click():
    new_text=my_input.get()
    my_label.config(text=new_text)


#Button
my_button=tkinter.Button(
    text="click me",
    command=button_click
)
my_button.grid(column=1,row=1)

#Entry
my_input=tkinter.Entry(width=20)
my_input.grid(column=0,row=1)


window.mainloop()
