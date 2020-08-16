from tkinter import *
from pygame import mixer

#initializing the window
window = Tk()
window.geometry('300x300')
window.title("Newzic Player")

mixer.init() #initializing pygame mixer

#functions for the start and stop buttons
def play_music():
    mixer.music.load("nani.mp3")
    mixer.music.play()

def stop_music():
    mixer.music.stop()


text = Label(window, text="Sample text I guess..")
text.pack()

#start and stop buttons
start_photo = PhotoImage(file='play.png')
play_btn = Button(window, image=start_photo, command=play_music)
play_btn.pack()

stop_photo = PhotoImage(file='stop.png')
stop_btn = Button(window, image=stop_photo, command=stop_music)
stop_btn.pack()











window.mainloop()
