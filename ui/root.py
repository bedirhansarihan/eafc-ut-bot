import tkinter as tk
from snipe_component import Snipe
from search_component import Search
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

PAD_X = 5
PAD_Y = 5

class Root(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Fifa Market Bot")
        self.geometry("1500x700")  # Set the size of the root window

        style = ThemedStyle(self)
        style.set_theme("equilux")  # Choose a theme, such as "equilux" or "plastik"

        self._top_frame = ttk.Frame(self)
        self._top_frame.pack(side=tk.TOP,fill=tk.BOTH, expand=True, padx=PAD_X, pady=PAD_Y)

        # Middle frame
        self._middle_frame = ttk.Frame(self, borderwidth=2, relief=tk.SOLID)
        self._middle_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=PAD_X, pady=PAD_Y)

        self._bottom_frame = ttk.Frame(self)
        self._bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=PAD_X, pady=PAD_Y)

        # Left frame
        self._left_frame = ttk.Frame(self._middle_frame, borderwidth=2, relief=tk.SOLID)
        self._left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=PAD_X, pady=PAD_Y)

        # Right frame
        self._right_frame = ttk.Frame(self._middle_frame, borderwidth=2)
        self._right_frame.pack(side=tk.RIGHT,fill=tk.BOTH, expand=True, padx=PAD_X, pady=PAD_Y)

        # Snipe component frame in the top left corner
        self._snipe_frame = Snipe(self._left_frame, borderwidth=2)
        self._snipe_frame.pack(fill=tk.BOTH, expand=True)

        # Search frame for search entry and button
        self._search_frame = Search(self._bottom_frame)
        self._search_frame.pack(side=tk.TOP, pady=PAD_Y)  # Place search components at the bottom

if __name__ == '__main__':
    root = Root()
    style = ThemedStyle(root)
    style.set_theme("arc")  # Choose a theme, such as "equilux" or "plastik"
    root.mainloop()