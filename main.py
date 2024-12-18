from tkinter import *
from cores.windows import *
import os
import sys
import traceback

def handle_exception(exc_type, exc_value, exc_tb):
    
    traceback.print_exception(exc_type, exc_value, exc_tb)

sys.excepthook = handle_exception

if __name__ == '__main__':
  MainWindow()