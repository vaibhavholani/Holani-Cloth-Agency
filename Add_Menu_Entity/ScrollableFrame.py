import tkinter as tk
from tkinter import ttk
from tkinter import *

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


root = tk.Tk()

frame = ScrollableFrame(root)

x = ["a", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "1","a", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "1"]

for pick in x:
    var = IntVar()
    chk = Checkbutton(frame, text=pick, variable=var)
    #var.trace("w", lambda *args, v=var: self.callback(var))
    chk.pack(side=TOP)

frame.pack()
root.mainloop()
