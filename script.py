from tkinter import *
import tkinter.messagebox
from pygame import mixer


#functions for the toolbar
def about_us():
    tkinter.messagebox.showinfo("About Newzic Player", "This is some random info.")

def close_window():
    window.destroy()

#functions for the start and stop buttons and the volume control
def play_music():
    mixer.music.load("nani.mp3")
    mixer.music.play()

def stop_music():
    mixer.music.stop()

def volume_control(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)




#initializing the window
window = Tk()
window.geometry('400x400')
window.title("Newzic Player")

#adding and configuring the toolbar/menubar
toolbar = Menu(window)
window.config(menu=toolbar)
#creating the sub-menu
submenu = Menu(toolbar, tearoff=0)
toolbar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open file")
submenu.add_command(label="Exit", command=close_window)

submenu = Menu(toolbar, tearoff=0)
toolbar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About Us", command=about_us)

mixer.init() #initializing pygame mixer for volume control



text = Label(window, text="Sample text I guess..")
text.pack()

#start and stop buttons
start_photo = PhotoImage(file='play.png')
play_btn = Button(window, image=start_photo, command=play_music)
play_btn.pack()

stop_photo = PhotoImage(file='stop.png')
stop_btn = Button(window, image=stop_photo, command=stop_music)
stop_btn.pack()

#adding a scale widget for volume control
scale = Scale(window, from_=0, to=100, orient = HORIZONTAL, command=volume_control)
scale.set(75)
scale.pack()











window.mainloop()
