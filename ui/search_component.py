import tkinter as tk
from tkinter import ttk
import json
from utils.search_player import search_player

PAD_X = 5
PAD_Y = 5


class Search(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._search_frame = ttk.Frame(self)
        self._search_frame.pack(side=tk.TOP)

        self._table_frame = ttk.Frame(self)
        self._table_frame.pack(side=tk.TOP)

        self._search_entry = ttk.Entry(self._search_frame, width=50)
        self._search_entry.pack(side=tk.LEFT, padx=PAD_X, pady=PAD_Y)

        self._search_button = ttk.Button(self._search_frame, text="Search", command=self._search)
        self._search_button.pack(side=tk.LEFT, padx=PAD_X, pady=PAD_Y)

        self._results_table = ttk.Treeview(self._table_frame, columns=("Player Name", "Rating", "Price", "Promo"))
        self._results_table.heading("#0", text="ID")
        self._results_table.heading("Player Name", text="Player Name")
        self._results_table.heading("Rating", text="Rating")
        self._results_table.heading("Price", text="Price")
        self._results_table.heading("Promo", text="Promo")
        self._results_table.pack(expand=True, fill=tk.BOTH)

    def _search(self):
        self._results_table.delete(*self._results_table.get_children())  # Clear existing data
        player_name = self._search_entry.get()

        player_data = search_player(player_name)

        for idx, player in enumerate(player_data, start=1):
            self._results_table.insert("", "end", text=str(idx), values=(player["name"], player["rating"], player["price"], player["promo"]))


if __name__ == '__main__':
    root = tk.Tk()
    search_frame = Search(root)
    search_frame.pack(expand=True, fill="both", padx=20, pady=20)
    root.mainloop()
