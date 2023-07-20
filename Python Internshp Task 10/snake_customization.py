import tkinter as tk
from tkinter import ttk, colorchooser
from tkinter import messagebox

selected_singleplayer_snake_color = (0, 255, 0)  
selected_multiplayer_snake_color1 = (255, 0, 0)  
selected_multiplayer_snake_color2 = (0, 0, 255) 

class CustomizationScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Snake Customization")
        self.root.geometry("300x300")

        self.label = ttk.Label(self.root, text="Choose Snake Color:")
        self.label.pack(pady=10)

        self.singleplayer_color_btn = ttk.Button(self.root, text="Select Single Player Color", command=self.choose_singleplayer_color, width=30)
        self.singleplayer_color_btn.pack(pady=10)

        self.label = ttk.Label(self.root, text="Select Multiplayer Snake Colors:")
        self.label.pack(pady=10)

        self.multiplayer_color_btn1 = ttk.Button(self.root, text="Select Player 1 Color", command=self.choose_multiplayer_color1, width=30)
        self.multiplayer_color_btn1.pack(pady=10)

        self.multiplayer_color_btn2 = ttk.Button(self.root, text="Select Player 2 Color", command=self.choose_multiplayer_color2, width=30)
        self.multiplayer_color_btn2.pack(pady=10)

        self.save_btn = ttk.Button(self.root, text="Save", command=self.save_colors, width=20)
        self.save_btn.pack(pady=10)

    def choose_singleplayer_color(self):
        global selected_singleplayer_snake_color
        _, color = colorchooser.askcolor(initialcolor="#%02x%02x%02x" % selected_singleplayer_snake_color)
        if color:
            try:
                selected_singleplayer_snake_color = tuple(int(c) for c in color)
            except:
                messagebox.showwarning("Error", "Customization doesn't work properly")

    def choose_multiplayer_color1(self):
        global selected_multiplayer_snake_color1
        _, color = colorchooser.askcolor(initialcolor="#%02x%02x%02x" % selected_multiplayer_snake_color1)
        if color:
            try:
                 selected_multiplayer_snake_color1 = tuple(int(c) for c in color)
            except:
                messagebox.showwarning("Error", "Customization doesn't work properly")

    def choose_multiplayer_color2(self):
        global selected_multiplayer_snake_color2
        _, color = colorchooser.askcolor(initialcolor="#%02x%02x%02x" % selected_multiplayer_snake_color2)
        if color:
            try:
                 selected_multiplayer_snake_color2 = tuple(int(c) for c in color)
            except:
                messagebox.showwarning("Error", "Customization doesn't work properly")

    def save_colors(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()