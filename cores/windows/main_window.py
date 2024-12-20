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
        file_menu.add_command(label="New Project", command=self.on_create_project_click)
        file_menu.add_command(label="Open Project", command=self.on_open_project_click)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.win.quit)

        view_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Show Toolbar")
        view_menu.add_command(label="Hide Toolbar")

        help_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")

        self.win.mainloop()

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