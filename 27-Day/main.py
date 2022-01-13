from tkinter import *

window = Tk()


window.title("My First GUI App")
window.minsize(width=500, height=300)

# components
label = Label(text="Label Test", font=("Arial", 18, "bold"))
# label.pack()
# label.pack(side='top')  # right, bottom, left, top
# label.pack(expand=True)
label.pack()

label['text'] = 'New Text Content'
label.config(text='New Text Content')


# BUTTON
def button_clicked():
    print("Clicked Me Someone")
    # label.config(text='Button Clicked')
    label.config(text=input.get())

button = Button(text='Click Me', command=button_clicked)
button.pack()



# ENTRY
input = Entry(width=20)
input.pack()
# print(input.get())

# data = input.get()
# print(data)


















# WINDOW SCREEN SHOW
window.mainloop()
