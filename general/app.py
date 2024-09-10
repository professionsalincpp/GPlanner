from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from constants import *
from .planner import Planner
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

        # Initialize main planner
        self.planner = Planner(self.main_frame)
        self.planner.pack(fill="both", expand=True)

    @property
    def mouse_coordinates(self):
        return self.planner.get_fixed_coords(self.planner.winfo_pointerx() - self.planner.winfo_rootx(), self.planner.winfo_pointery() - self.planner.winfo_rooty())

    def run(self):
        self.update_planner()
        self.planner.bind("<Motion>", self.on_mouse_pos_change)
        self.root.mainloop()

    def update_planner(self):
        self.planner.delete("all")
        img = ImageTk.PhotoImage(Image.open("class_dark.png"))
        self.planner.create_image(0, 0, anchor="nw", image=img)
        self.planner.image = img
        x, y = self.mouse_coordinates
        self.planner.create_text(*self.planner.get_fixed_coords(-100, -50), text=f"X: {x}, Y: {y}", font=("Consolas", 14))
        self.planner.after(100, self.update_planner)

    def on_mouse_pos_change(self, event):
        print(self.mouse_coordinates)
