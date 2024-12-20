from tkinter import *
from tkinter.ttk import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog
from cores.components.project_view import *
from cores.services import *
from .create_project_window import CreateProjectWindow


class ProjectEditWindow:
    def __init__(self, project):
        self.current_project = project
        self.win = Toplevel()
        self.win.geometry("1000x600")
        self.win.title(f"{project.name} | Project editor | Genealyze")
        self.menu = Menu(self.win)
        self.win.config(menu=self.menu)

        file_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Project",command=self.on_open_project_click,)
        file_menu.add_command(label="New Project", command=self.on_create_project_click)
        file_menu.add_command(label="Quit",command=self.on_quit_click)
        file_menu.add_separator()

        self.project_view = ProjectView(self.win)
        self.project_view.treeview.grid(row=0,column=0,ipadx=50)
        
        
    def on_quit_click(self):
        self.win.destroy()
    
    def on_create_project_click(self):
        win = CreateProjectWindow()
        win.on_created = lambda project : ProjectEditWindow(win.project)

    def on_open_project_click(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            ProjectEditWindow(
              ProjectManageService.get_project(folder_selected)
            )