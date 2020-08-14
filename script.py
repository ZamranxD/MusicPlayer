from tkinter import *


window = Tk()
window.geometry('300x300')
window.title("Newzic Player")

text = Label(window, text="Sample text I guess..")
text.pack()

photo = PhotoImage(file='play-button.png')
photolabel = Label(window, image=photo)
photolabel.pack()

window.mainloop()