from PIL import Image, ImageTk
from tkinter import *
import os

current_dir = os.path.dirname(__file__)

def loadIcon(name):
  return PhotoImage(width=40, height=40,file=os.path.join(current_dir, f"../../data/icons/{name}.png")) 