from tkinter import *
from tkinter.filedialog import askopenfile 
from tkinter.filedialog import *
import os
import fnmatch
from pygame import mixer

Canvas = Tk()
Canvas.title ("play music")
Canvas.geometry("500x500")
Canvas.config (bg = "white")

"""def openfiles():
    global chemin_lecture
    chemin_lecture = askopenfilename(title="Selectionner le fichier", filetypes =[("all files","*.mp3")])
"""
chemin_lecture = r"C:\\Users\adabi\OneDrive\Bureau\la plateforme\Player-Music\playlist"
#folder = 
pattern = "mp4"
mixer.init() #initialiser  le son

img_precedent = PhotoImage(file="prev.png")
img_stop = PhotoImage(file="stop.png")
img_play = PhotoImage(file="play.png")
img_pause = PhotoImage(file="pause.png")
img_suivant = PhotoImage(file="next.png")

def select():
    #label.config(text=list_lecture.get("anchor"))
    #Retrieve()  
    #mixer.music.load(chemin_lecture+"\\"+list_lecture.get("anchor"))
    #folder = chemin_lecture+"\playlist"
    #mixer.music.load(chemin_lecture + "Midadi.mp3")
    music = list_lecture.get(ACTIVE)
    mixer.music.load(chemin_lecture + "\\" + list_lecture.get(ACTIVE))
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
    mixer.music.load(chemin_lecture+"\\"+nom_son_suivant)
    mixer.music.play()

    list_lecture.select_clear(0,"end")
    list_lecture.activate(son_suivant)
    list_lecture(son_suivant)

def precedent():
    son_precedent = list_lecture.curselection()
    son_precedent = son_precedent[0]-1
    nom_son_precedent = list_lecture.get(son_precedent)

    label.config(text=nom_son_precedent)
    mixer.music.load(chemin_lecture+"\\"+nom_son_precedent)
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

#selection = Button(Canvas, text="selection son", bg = "white", borderwidth=0, command=openfiles)
#selection.pack(pady=15, in_=top, side=LEFT)

"""for files in os.walk(chemin_lecture):
    print("list", files)
    for filename in fnmatch.filter(files,pattern):
        list_lecture.insert("end", filename)
"""
#def Retrieve():
for files in os.listdir(chemin_lecture):
    if files.endswith(pattern):
        list_lecture.insert(1, files)
#return list_lecture

"""
folder = r"C:\\Users\adabi\OneDrive\Bureau\la plateforme\Player-Music\playlist"
file = os.listdir(folder)
#filesmp3 = files.endswith(".mp3")
#print("LIST: ", file)
print(list_lecture)

list_lecture.insert(1, file)
"""
#Retrieve()
Canvas.mainloop()