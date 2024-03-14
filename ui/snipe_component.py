import tkinter as tk
import tkinter.ttk as ttk


class Snipe(ttk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._snipe_label = ttk.Label(self, text="Snipe Player", font=('Arial', 18))
        self._snipe_label.grid(row=0, columnspan=2, pady=10)

        self._max_buy_now_price_label = ttk.Label(self, text="Max Buy Now Price:", font=('Arial', 16))
        self._max_buy_now_price_label.grid(row=1, column=0, padx=5, pady=5)
        self._max_buy_now_price_entry = ttk.Entry(self, width=20)
        self._max_buy_now_price_entry.grid(row=1, column=1, padx=5, pady=5)

        self._interval_time_label = ttk.Label(self, text="Interval Time (s):", font=('Arial', 16))
        self._interval_time_label.grid(row=2, column=0, padx=5, pady=5)
        self._interval_time_entry = ttk.Entry(self, width=20)
        self._interval_time_entry.grid(row=2, column=1, padx=5, pady=5)