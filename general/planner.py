from customtkinter import *
    
class Planner(CTkCanvas):
    def __init__(self, parent, width=800, height=600, bg_color="#ffffff") -> None:
        super().__init__(parent, width=width, height=height, bg=bg_color)
        
        self.objects: list = []
        self._drag_start: tuple = (0, 0)
        self._dragging: bool = False
        self._id = 0
        self.bind_events()
    
    def bind_events(self) -> None:
        """
        Bind events to the planner.

        The events currently bound are:

        - `<ButtonPress-1>`: calls `_on_drag_starts`
        - `<ButtonRelease-1>`: calls `_on_drag_ends`
        """
        self.bind("<ButtonPress-1>", self._on_drag_starts)
        self.bind("<ButtonRelease-1>", self._on_drag_ends)
        self.bind("<B1-Motion>", self._on_drag_motion)

    def get_width(self) -> int:
        """
        Returns the width of the planner in pixels.

        :return: Width of the planner in pixels
        :rtype: int
        """
        return self.winfo_width()
    
    def get_height(self) -> int:
        """
        Returns the height of the planner in pixels.

        :return: Height of the planner in pixels
        :rtype: int
        """
        return self.winfo_height()
    
    def get_size(self) -> tuple:
        """
        Returns the size of the planner in pixels as a tuple of two integers.

        The first element of the tuple is the width of the planner in pixels.
        The second element of the tuple is the height of the planner in pixels.

        :return: Size of the planner in pixels
        :rtype: tuple
        """
        return self.winfo_x(), self.winfo_y()
    
    def get_fixed_coords(self, x: int, y: int) -> tuple:
        """
        Returns the coordinates (x, y) translated to the fixed coordinates system.
        In the fixed coordinates system, the origin is at the top-left corner of the
        planner, and the x and y axes are directed to the right and down, respectively.
        The coordinates are translated by adding the width and height of the planner
        to the negative coordinates. This is useful when dealing with the mouse
        coordinates, which are relative to the root window.
        
        :param x: X coordinate in the planner
        :param y: Y coordinate in the planner
        :return: Coordinates in the fixed coordinates system
        :rtype: tuple
        """
        return x if x >= 0 else x + self.get_width(), y if y >= 0 else y + self.get_height()
    
    @property
    def mouse_coordinates(self):
        """
        Property that returns the mouse coordinates in the fixed coordinates system.
        
        The fixed coordinates system is a coordinate system in which the origin is at the top-left corner of the planner,
        and the x and y axes are directed to the right and down, respectively. This is useful when dealing with the mouse
        coordinates, which are relative to the root window.
        
        :return: Mouse coordinates in the fixed coordinates system
        :rtype: tuple
        """
        return self.get_fixed_coords(self.winfo_pointerx() - self.winfo_rootx(), self.winfo_pointery() - self.winfo_rooty())        
    
    @property
    def dragging(self) -> bool:
        """
        Property that returns whether the planner is currently being dragged.
        
        :return: Whether the planner is currently being dragged
        :rtype: bool
        """
        return self._drag_start is not None
        
    def _on_drag_starts(self, event):
        self._drag_start = (event.x, event.y)

    def _on_drag_ends(self, event):
        self._drag_start = None
        self._dragging = False

    def _on_drag_motion(self, event):
        self._dragging = True
        print(f'dragging from {self._drag_start} to {self.mouse_coordinates}')