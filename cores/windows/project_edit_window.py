from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from .create_project_window import CreateProjectWindow


class ProjectEditWindow:
    def __init__(self, project):
        self.current_project = project
        self.win = Tk()
        self.win.geometry("1000x600")
        self.win.title(f"{project.name} | Project editor | Genealyze")
        self.menu = Menu(self.win)
        self.win.config(menu=self.menu)

        file_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Project")
        file_menu.add_command(label="New Project", command=self.create_project)
        file_menu.add_command(label="Save Project")
        file_menu.add_separator()


    def create_project(self):
        CreateProjectWindow()
