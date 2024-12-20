from tkinter import *
from tkinter.ttk import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog
from cores.helpers.image import loadIcon
import os


class ProjectView:
    def __init__(self, root):
        Style().configure("Treeview", rowheight=50)
        self.root = root
        self.treeview = Treeview(root)
        self.treeview.pack(expand=True)
        self.icons =[
          loadIcon("seq_icon")
        ]

        self.seq_treeview_item = self.treeview.insert(
            "", END, text="Sequences", image=self.icons[0],
        )
        
        self.assets_treeview_item = self.treeview.insert(
            "", END, text="Assets",
        )

