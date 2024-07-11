import tkinter

window = tkinter.Tk()
window.title("Simple GUI App")
window.minsize(width=500,height=300)


#Label
my_label=tkinter.Label(
    text="first label",
    font=("Arial",24, "bold")
)

def button_click():
    my_label.config(text="button got click")


#Button
my_button=tkinter.Button(
    text="click me",
    command=button_click
)

my_input=tkinter.Entry(width=20)

my_label.pack()
my_button.pack()
my_input.pack()


window.mainloop()
