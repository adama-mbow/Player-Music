from tkinter import *
from tkinter.filedialog import askopenfile 
from tkinter import filedialog
from tkinter.filedialog import *
import time
#from mutagen.mp3 import MP3
import os
import fnmatch
from pygame import mixer

Canvas = Tk()
Canvas.title ("play music")
Canvas.geometry("500x500")
Canvas.config (bg = "white")

"""def openfiles():
    global mp3_files
    global path
    path = askopenfilename( )
    os.chdir(path)
    playlist = os.listdir(path)
    mp4_files = [files for files in playlist if files.endswith("*.mp4")]
    for files in mp3_files:
        list_lecture.insert(END, files)
        print(files)
        print(mp4_files)"""

def add_song():
    global song
    song = filedialog.askopenfilename(initialdir='\musique', title='Choose the songs to import', filetypes=(("mp3 Files", "*.mp3"), ))
   
    #Enlever l'affichage du chemin dans la listbox pour garder uniquement le titre
    song = song.replace (".mp3", "")

    #inserer la musique dans la listbox
    list_lecture.insert(END,song)
mixer.init() #initialiser  le son

img_precedent = PhotoImage(file="prev.png")
img_stop = PhotoImage(file="stop.png")
img_play = PhotoImage(file="play.png")
img_pause = PhotoImage(file="pause.png")
img_suivant = PhotoImage(file="next.png")

def select():
    label.config(text=list_lecture.get("anchor"))
    #Retrieve()  
    mixer.music.load(song+"\\"+list_lecture.get("anchor"))
    #folder = chemin_lecture+"\playlist"
    mixer.music.load(song)
    music = list_lecture.get(ACTIVE)
    mixer.music.load(song + "\\" + list_lecture.get(ACTIVE))
    mixer.music.play()
    
def stop():
    mixer.music.stop()
    list_lecture.select_clear("active")

def pause():
    if pauseboutton["text"] == "pause":
        mixer.music.pause()
        pauseboutton["text"] == "play"
    else:
        mixer.music.unpause()
        pauseboutton["text"] = "pause"

def suivant():
    son_suivant = list_lecture.curselection()
    son_suivant = son_suivant[0]+1
    nom_son_suivant = list_lecture.get(son_suivant)

    label.config(text=nom_son_suivant)
    mixer.music.load(song+"\\"+nom_son_suivant)
    mixer.music.play()

    list_lecture.select_clear(0,"end")
    list_lecture.activate(son_suivant)
    list_lecture(son_suivant)

def precedent():
    son_precedent = list_lecture.curselection()
    son_precedent = son_precedent[0]-1
    nom_son_precedent = list_lecture.get(son_precedent)

    label.config(text=nom_son_precedent)
    mixer.music.load(song+"\\"+nom_son_precedent)
    mixer.music.play()

    list_lecture.select_clear(0,"end")
    list_lecture.activate(son_precedent)
    list_lecture(son_precedent)

list_lecture = Listbox(Canvas,fg="cyan",bg="black", width=100, font=("poppin", 14))
list_lecture.pack(padx=15, pady=15)


label = Label(Canvas, text="", bg="white", fg="black", font=("poppin", 18))
label.pack(pady=15)
top = Frame(Canvas, bg="white")
top.pack(padx=10, pady=15, anchor="center")

precedentboutton = Button(Canvas, text="precedent", image=img_precedent, bg = "white", borderwidth=0, command=precedent)
precedentboutton.pack(pady=15, in_=top, side=LEFT)
stopboutton = Button(Canvas, text="stop",image=img_stop, bg = "white", borderwidth=0, command=stop)
stopboutton.pack(pady=15, in_=top, side=LEFT)
playboutton = Button(Canvas, text="play",image=img_play, bg = "white", borderwidth=0, command=select)
playboutton.pack(pady=15, in_=top, side=LEFT)
pauseboutton = Button(Canvas, text="pause",image=img_pause, bg = "white", borderwidth=0, command=pause)
pauseboutton.pack(pady=15, in_=top, side=LEFT)
suivantboutton = Button(Canvas, text="suivant",image=img_suivant, bg = "white", borderwidth=0, command=suivant)
suivantboutton.pack(pady=15, in_=top, side=LEFT)

selection = Button(Canvas, text="selection son", bg = "white", borderwidth=0, command=add_song)
selection.pack(pady=15, in_=top, side=LEFT)


#openfiles()
#Retrieve()
Canvas.mainloop()