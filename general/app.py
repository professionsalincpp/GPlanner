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
from math import *

import math

def find_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dy, dx)
    return math.degrees(angle)


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

    
    def run(self):
        self.update_planner()
        self.planner.bind("<Motion>", self.on_mouse_pos_change)
        self.root.mainloop()

    def update_planner(self):
        self.planner.delete("all")
        img = ImageTk.PhotoImage(Image.open("class_dark.png"))
        self.planner.create_image(0, 0, anchor="nw", image=img)
        self.planner.image = img
        if self.planner._dragging:
            self.planner.create_text(*self.planner.get_fixed_coords(-200, -100), text=f"Dragging from {self.planner._drag_start} to {self.planner.mouse_coordinates}", font=("Consolas", 14))
            self.planner.create_line(*self.planner.get_fixed_coords(*self.planner._drag_start), *self.planner.get_fixed_coords(*self.planner.mouse_coordinates), fill="red", width=2)
            _angle = find_angle(*self.planner._drag_start, *self.planner.mouse_coordinates)
            _label_pos = ((self.planner._drag_start[0] + self.planner.mouse_coordinates[0]) / 2, 
                        (self.planner._drag_start[1] + self.planner.mouse_coordinates[1]) / 2)
            _label_pos = (_label_pos[0], _label_pos[1] - 20 * math.sin(math.radians(_angle)))
            self.planner.create_text(*_label_pos, angle=-_angle, text=f"Distance: {round(dist(self.planner._drag_start, self.planner.mouse_coordinates), 2)}", font=("Consolas", 16, "italic"),)
        x, y = self.planner.mouse_coordinates
        self.planner.create_text(*self.planner.get_fixed_coords(-100, -50), text=f"X: {x}, Y: {y}", font=("Consolas", 14))
        self.planner.after(10, self.update_planner)

    def on_mouse_pos_change(self, event):
        print(self.planner.mouse_coordinates)
