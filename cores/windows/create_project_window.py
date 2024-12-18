from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from cores.services import *
from .status_window import *
import time


class CreateProjectWindow:
    def __init__(self):
        self.win = Tk()
        self.win.title("Create New Project | Genealyze")
        self.win.geometry("1244x367")
        self.win.grid_rowconfigure(0, weight=1)
        self.win.grid_rowconfigure(1, weight=1)
        self.win.grid_rowconfigure(2, weight=1)
        self.win.grid_rowconfigure(3, weight=1)
        self.win.grid_columnconfigure(0, weight=1)
        self.win.grid_columnconfigure(1, weight=2)
        self.win.resizable(False,False)
        
        self.project_name_label = Label(self.win, text="Project Name:")
        self.project_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        
        self.project_name_entry = Entry(self.win, width=30)
        self.project_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.select_location_label = Label(self.win, text="Location:")
        self.select_location_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        
        self.location_entry = Entry(self.win, width=30)
        self.location_entry.grid(row=1, column=1, padx=10, pady=5)

        self.btn_frame = Frame(self.win)
        self.btn_frame.grid(row=3, column=1)
        self.select_location_button = Button(self.btn_frame, text="Choose Location", command=self.select_location)
        self.select_location_button.grid(row=2, column=1, pady=5, sticky="w")

        self.create_button = Button(self.btn_frame, text="Create Project", command=self.create_project)
        self.create_button.grid(row=2, column=2,padx=10, pady=10)
        
        self.project = None
    def select_location(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.location_entry.delete(0, END)
            self.location_entry.insert(0, folder_selected)
            self.selected_location = folder_selected

    def on_created(self, project ):
      pass
    
    def create_project(self):
        project_name = self.project_name_entry.get()
        if project_name and hasattr(self, 'selected_location'):
            self.win.destroy()
            win = StatusWindow("Creating project ...")
            self.project = ProjectManage.create_project(project_name,self.selected_location)
            win.close()
            self.on_created(self.project)
        else:
            messagebox.showerror("Error","Please enter a project name and select a location.")

  