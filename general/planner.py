from customtkinter import *

class Planner(CTkCanvas):
    def get_width(self) -> int:
        return self.winfo_width()
    
    def get_height(self) -> int:
        return self.winfo_height()
    
    def get_size(self) -> tuple:
        return self.winfo_x(), self.winfo_y()
    
    def get_fixed_coords(self, x: int, y: int) -> tuple:
        return x if x >= 0 else x + self.get_width(), y if y >= 0 else y + self.get_height()