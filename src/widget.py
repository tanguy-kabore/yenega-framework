import os
from tkinter import Tk, Label, Entry, Button, Frame, BOTH
from PIL import ImageTk, Image
import screeninfo # Script to intall library: pip install screeninfo
from env import *

class Widget:

    @staticmethod
    def TextLabel(root, label, color, font):
        return Label(root, text=label, fg=color, font=(font))

    @staticmethod
    def TextEntry(root, color, font, type):
        if type == 'text':
            return Entry(root, fg=color, font=(font), show='')
        elif type == 'password':
            return Entry(root, fg=color, font=(font), show='*')
        else:
            return None
    
    @staticmethod
    def TextButton(root, label, font):
        return Button(root, text=label, font=(font),  bg= PRIMARY_COLOR, fg='white')
    
    @staticmethod
    def Screen(ratio, row_number, column_number, resizable):
        screen= Tk()
        # Define the resize ratio
        resize_ratio = ratio  # Example: Resizes the window to half of the screen size
        # Get the device screen dimensions
        screen_info = screeninfo.get_monitors()[0] # Get device screen info
        screen_width = screen_info.width
        screen_height = screen_info.height
        # Calculate the desired width and height for the window
        window_width = int(screen_width * resize_ratio)
        window_height = int(screen_height * resize_ratio)
        # Calculate the x and y coordinates to center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        screen.title(APP_NAME)
        # Get the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Navigate up two directories to reach the project directory
        project_dir = os.path.abspath(os.path.join(current_dir, '..'))
        # Load the icon image and resize if necessary
        icon_image = Image.open(project_dir+LOGO_ICO)
        icon_image = icon_image.resize((32, 32), Image.ANTIALIAS)
        # Create a PhotoImage object from the resized image
        icon_photo = ImageTk.PhotoImage(icon_image)
        screen.iconphoto(True, icon_photo)
        screen.configure(bg=BACKGROUND_COLOR)
        if resizable == False:
            screen.resizable(False, False)
        else:
            screen.resizable(True, True)
        # Set the window geometry
        screen.geometry(f"{window_width}x{window_height}+{x}+{y}")
        # Configure rows and columns to resize proportionally
        for i in range(row_number):  # Number of rows
            screen.grid_rowconfigure(i, weight=1)
        for j in range(column_number):  # Number of columns
            screen.grid_columnconfigure(j, weight=1)
        return screen

    @staticmethod
    def create_frame(master, bg, row_number, column_number):
        frame = Frame(master, bg=bg)
        frame.grid(sticky='nsew')
        for i in range(row_number):  # Configure rows to resize proportionally
            frame.grid_rowconfigure(i, weight=1)
            
        for j in range(column_number):  # Configure columns to resize proportionally
            frame.grid_columnconfigure(j, weight=1)
        
        return frame