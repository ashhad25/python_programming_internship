import tkinter as tk
import subprocess
import os

def play_audio():
    current_dir = os.getcwd()
    audio_file = os.path.join(current_dir, "play_audio.py")
    subprocess.run(["python", audio_file])

def play_video():
    current_dir = os.getcwd()
    video_file = os.path.join(current_dir, "play_video.py")
    subprocess.run(["python", video_file])

# Create the main window
window = tk.Tk()
window.geometry("300x100")
window.title("Select A Player")

# Create the buttons
audio_button = tk.Button(window, text="Open Audio Player", command=play_audio)
audio_button.pack(pady=10)

video_button = tk.Button(window, text="Open Video Player", command=play_video)
video_button.pack(pady=10)

# Run the main event loop
window.mainloop()