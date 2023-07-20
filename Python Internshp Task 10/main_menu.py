import tkinter as tk
from tkinter import ttk
import subprocess
from snake_customization import CustomizationScreen

def run_singleplayer():
    subprocess.run(["python", "singleplayer.py"])
    root.destroy()

def run_multiplayer():
    subprocess.run(["python", "multiplayer.py"])
    root.destroy()

def run_customization():
    customization_screen = CustomizationScreen()
    customization_screen.run()

def run_exit():
    root.destroy()

def main():
    global root
    root = tk.Tk()
    root.title("Snake Game - Main Screen")
    root.geometry("400x300")
    root.configure(bg="#333333")

    label = tk.Label(root, text="Snake Game Menu", font=("Arial", 20), bg="#333333", fg="white")
    label.pack(pady=20)

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), foreground="black", background="#444444")
    
    singleplayer_btn = ttk.Button(root, text="Single Player", command=run_singleplayer, width=20)
    singleplayer_btn.pack(pady=10)

    multiplayer_btn = ttk.Button(root, text="Multiplayer", command=run_multiplayer, width=20)
    multiplayer_btn.pack(pady=10)

    customization_btn = ttk.Button(root, text="Snake Customization", command=run_customization, width=20)
    customization_btn.pack(pady=10)

    exit_btn = ttk.Button(root, text="Exit", command=run_exit, width=20)
    exit_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
