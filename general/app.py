from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from constants import *
import os
import shutil

class GPlanner(object):
    def __init__(self):
        # Initialize the Tkinter window
        self.root = CTk()
        self.root.geometry(GEOMETRY)
        self.root.title(TITLE)

        # Initialize the main frame
        self.main_frame = CTkFrame(self.root, **DEFAULT_FRAME_STYLE)
        self.main_frame.pack(fill="both", expand=True)

        # Initialize the top frame
        self.top_frame = CTkFrame(self.main_frame, **TOP_FRAME_STYLE, height=30)
        self.top_frame.pack(fill="x", side="top")

        # Initialize main canvas
        self.canvas = CTkCanvas(self.main_frame)
        self.canvas.pack(fill="both", expand=True)

    def run(self):
        self.update_canvas()
        self.canvas.bind("<Motion>", self.on_mouse_pos_change)
        self.root.mainloop()

    def update_canvas(self):
        self.canvas.delete("all")
        img = ImageTk.PhotoImage(Image.open("class_dark.png"))
        self.canvas.create_image(0, 0, anchor="nw", image=img)
        self.canvas.image = img
        self.canvas.after(100, self.update_canvas)

    def on_mouse_pos_change(self, event):
        print(event.x, event.y)

