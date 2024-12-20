from tkinter import *
from tkinter.ttk import Progressbar

class StatusWindow:
    def __init__(self, title="Status Window"):
        self.root = Toplevel()
        self.root.overrideredirect(True)

        self.status_label = Label(self.root, text=title, width=40, height=2)
        self.status_label.pack(pady=20)

        self.progress = Progressbar(self.root, orient=HORIZONTAL, length=300,)
        self.progress.pack(pady=20)
        self.start_progress()
    
    def close(self):
       self.root.destroy()
       
    def start_progress(self):
        self.progress.start()

