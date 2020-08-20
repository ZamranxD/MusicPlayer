from tkinter import *
import tkinter.messagebox
from pygame import mixer
import tkinter.filedialog
import os
import pause

#functions for the toolbar
def about_us():
    tkinter.messagebox.showinfo("About Newzic Player", "This is some random info.")

def close_window():
    window.destroy()

def browse():
    global filename
    filename = tkinter.filedialog.askopenfilename()

#functions for the play, pause and stop buttons and the volume control
def play_music():
    if pause.paused == False:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            status_bar['text'] = f"Playing music - {os.path.basename(filename)}"
        except:
            tkinter.messagebox.showerror("No file selected", "Please make sure to open a file first before clicking play.")
    elif pause.paused==True:
        mixer.music.unpause()
        status_bar['text'] = f"Playing music - {os.path.basename(filename)}"


def stop_music():
    pause.paused = False
    mixer.music.stop()
    status_bar['text'] = f"{os.path.basename(filename)} Stopped"


def volume_control(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

def pause_music():
    pause.paused = True
    mixer.music.pause()
    status_bar['text'] = "Music paused"




#initializing the window
window = Tk()
window.title("Newzic Player")

#adding and configuring the toolbar/menubar
toolbar = Menu(window)
window.config(menu=toolbar)
#creating the sub-menu
submenu = Menu(toolbar, tearoff=0)
toolbar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open file", command=browse)
submenu.add_command(label="Exit", command=close_window)

submenu = Menu(toolbar, tearoff=0)
toolbar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About Us", command=about_us)

mixer.init() #initializing pygame mixer for volume control



text = Label(window, text="Sample text I guess..")
text.pack(pady=10)

#making a new frame(div)to group these buttons together
midFrame = Frame(window)
midFrame.pack(padx=60, pady=7) 
#play, pause and stop buttons
start_photo = PhotoImage(file='play.png')
play_btn = Button(midFrame, image=start_photo, command=play_music)
play_btn.pack(side=LEFT, padx=5)

stop_photo = PhotoImage(file='stop.png')
stop_btn = Button(midFrame, image=stop_photo, command=stop_music)
stop_btn.pack(side=LEFT, padx=5)

pause_photo = PhotoImage(file='pause.png')
pause_btn = Button(midFrame, image=pause_photo, command=pause_music)
pause_btn.pack(side=LEFT, padx=5)

#adding a scale widget for volume control
scale = Scale(window, from_=0, to=100, orient = HORIZONTAL, command=volume_control)
scale.set(75)
scale.pack()





#adding a statusbar at the bottom
status_bar = Label(window, text="Welcome to Newzic Player", relief=SUNKEN)
status_bar.pack(side=BOTTOM, fill=X)





window.mainloop()
