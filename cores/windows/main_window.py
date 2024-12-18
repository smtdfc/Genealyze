from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from .create_project_window import *
from .project_edit_window import * 

class MainWindow:
    def __init__(self):
        self.current_project = None
        self.win = Tk()
        self.win.title("Genealyze")
        self.menu = Menu(self.win)
        self.win.config(menu=self.menu)

        file_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project", command=self.create_project)
        file_menu.add_command(label="Open Project", command=self.open_file)
        file_menu.add_command(label="Save Project", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.win.quit)

        view_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Show Toolbar")
        view_menu.add_command(label="Hide Toolbar")

        help_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        self.win.mainloop()

    def create_project(self):
        win = CreateProjectWindow()
        win.on_created = lambda project : ProjectEditWindow(win.project)
        
   
    def open_file(self,path):
      pass
    
    def open_project(self):
        pass

    def save_file(self):
        pass

    def show_about(self):
        pass

