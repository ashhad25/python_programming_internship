from tkinter import *
import tkinter.font as font
from tkinter import filedialog
from tkinter import messagebox
import vlc

def add_videos():
    video_files = filedialog.askopenfilenames(initialdir="Videos/", title="Choose Video File",filetypes=(("Video Files", "*.mp4 *.mkv"),))
    for video_file in video_files:
        videos_list.insert(END, video_file)

def delete_video():
    selected_video = videos_list.curselection()
    if videos_list.size() == 0:
        show_message("Empty Playlist", "There are no videos in the playlist.")
        return
    if not selected_video:
        show_message("No Video Selected", "Please select a video to delete.")
        return
    videos_list.delete(selected_video[0])
    if videos_list.size() > 0:
        videos_list.selection_clear(0, END)
        videos_list.selection_set(selected_video[0])
        messagebox.showinfo("Video Deleted", "The selected video has been deleted.")
    else:
        messagebox.showinfo("Empty Playlist", "The playlist is now empty.")
    
def play_video():
    if not videos_list.curselection():
        videos_list.selection_set(0)

    video = videos_list.get(ACTIVE)
    if not video:
        show_message("Error", "No videos in the playlist.")
        return
    media = vlc.Media(video)
    media_player.set_media(media)
    media_player.play()

def pause_video():
    media_player.pause()

def stop_video():
    media_player.stop()

def resume_video():
    media_player.set_pause(0)

def previous_video():
    if videos_list.size() == 0:
        show_message("Empty Playlist", "There are no videos in the playlist.")
        return
    if media_player.is_playing():
        media_player.stop()
    previous_one = videos_list.curselection()
    if previous_one:
        previous_one = previous_one[0] - 1
        if previous_one >= 0:
            videos_list.selection_clear(0, END)
            videos_list.activate(previous_one)
            videos_list.selection_set(previous_one)
            videos_list.get(ACTIVE)
            play_video()
        else:
            show_message("No Previous Song", "This is the first video in the playlist.")


def next_video():
    if videos_list.size() == 0:
        show_message("Empty Playlist", "There are no videos in the playlist.")
        return
    if media_player.is_playing():
        media_player.stop()
    next_one = videos_list.curselection()
    if next_one:
        next_one = next_one[0] + 1
        if next_one < videos_list.size():
            videos_list.selection_clear(0, END)
            videos_list.activate(next_one)
            videos_list.selection_set(next_one)
            videos_list.get(ACTIVE)
            play_video()
        else:
            show_message("No Next Song", "This is the last video in the playlist.")


def show_message(title, message):
    messagebox.showwarning(title, message)

root = Tk()
root.title('Audio/Video Player')

instance = vlc.Instance()
media_player = instance.media_player_new()

videos_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15),height=12, width=47, selectbackground="gray", selectforeground="black")
videos_list.grid(columnspan=6)

defined_font = font.Font(family='Helvetica')

add_videos_button = Button(root, text="Add Videos", width=10, command=add_videos)
add_videos_button['font'] = defined_font
add_videos_button.grid(row=1, column=0)

delete_video_button = Button(root, text="Delete Video", width=10, command=delete_video)
delete_video_button['font'] = defined_font
delete_video_button.grid(row=1, column=1)

play_button = Button(root, text="Play", width=7, command=play_video)
play_button['font'] = defined_font
play_button.grid(row=1, column=2)

pause_button = Button(root, text="Pause", width=7, command=pause_video)
pause_button['font'] = defined_font
pause_button.grid(row=1, column=3)

stop_button = Button(root, text="Stop", width=7, command=stop_video)
stop_button['font'] = defined_font
stop_button.grid(row=1, column=4)

resume_button = Button(root, text="Resume", width=7, command=resume_video)
resume_button['font'] = defined_font
resume_button.grid(row=1, column=5)

previous_button = Button(root, text="Prev", width=7, command=previous_video)
previous_button['font'] = defined_font
previous_button.grid(row=2, column=2)

next_button = Button(root, text="Next", width=7, command=next_video)
next_button['font'] = defined_font
next_button.grid(row=2, column=3)

root.mainloop()
