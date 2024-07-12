import tkinter

window=tkinter.Tk()

window.title("hello")
window.minsize(width=500,height=500)

my_label=tkinter.Label(text="Label")
my_label.grid(column="0",row="0")

my_input=tkinter.Entry()
my_input.grid(column="0",row="1")

def click():
    text=my_input.get()
    my_label.config(text=text)

my_btn=tkinter.Button(text="button", command=click)
my_btn.grid(column="1",row="1")

window.mainloop()

def add(*args):
    temp=0
    for i in args:
        temp+=i
    return temp

print(add(1,2,3,4,5,))

def add2(**kwargs):
    temp=kwargs["a"]+kwargs["b"]
    return temp

print(add2(a=12,b=22))