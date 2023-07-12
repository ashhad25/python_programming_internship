from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
from tkinter import messagebox


def addsongs():
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    for s in temp_song:
        songs_list.insert(END,s)
        
            
def deletesong():
    selected_song = songs_list.curselection()
    if songs_list.size() == 0:
        show_message("Empty Playlist", "There are no songs in the playlist.")
        return
    if not selected_song:
        show_message("No Song Selected", "Please select a song to delete.")
        return
    songs_list.delete(selected_song[0])
    if songs_list.size() > 0:
        songs_list.selection_clear(0, END)
        songs_list.selection_set(selected_song[0])
        messagebox.showinfo("Song Deleted", "The selected song has been deleted.")
    else:
        messagebox.showinfo("Empty Playlist", "The playlist is now empty.")
    
    
def Play():
    if not songs_list.curselection():
        songs_list.selection_set(0)

    song = songs_list.get(ACTIVE)
    if not song:
        show_message("Error", "No songs in the playlist.")
        return
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def Resume():
    mixer.music.unpause()

def Previous():
    if mixer.music.get_busy():
        mixer.music.stop()
    if songs_list.size() == 0:
        show_message("Empty Playlist", "There are no songs in the playlist.")
        return
    previous_one = songs_list.curselection()
    if previous_one:
        previous_one = previous_one[0] - 1
        if previous_one >= 0:
            songs_list.selection_clear(0, END)
            songs_list.activate(previous_one)
            songs_list.selection_set(previous_one)
            mixer.music.load(songs_list.get(ACTIVE))
            mixer.music.play()
        else:
            show_message("No Previous Song", "This is the first song in the playlist.")

def show_message(title, message):
    messagebox.showwarning(title, message)

def Next():
    if mixer.music.get_busy():
        mixer.music.pause()
    if songs_list.size() == 0:
        show_message("Empty Playlist", "There are no songs in the playlist.")
        return
    next_one = songs_list.curselection()
    if next_one:
        next_one = next_one[0] + 1
        if next_one < songs_list.size():
            songs_list.selection_clear(0, END)
            songs_list.activate(next_one)
            songs_list.selection_set(next_one)
            mixer.music.load(songs_list.get(ACTIVE))
            mixer.music.play()
        else:
            show_message("No Next Song", "This is the last song in the playlist.")


root=Tk()
root.title('Audio/Video Player')
mixer.init()

songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=6)

defined_font = font.Font(family='Helvetica')

play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

previous_button=Button(root,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)

my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Select Audio",command=addsongs)
add_song_menu.add_command(label="Delete Audio",command=deletesong)


mainloop()