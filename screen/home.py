from tkinter import Menu, messagebox
from src.widget import Widget
from translation import *

class HomeScreen:
    def __init__(self):
        self.root = Widget.Screen(1, 1, 1, True)
        # Create menu bar
        self.menu_bar = Menu(self.root)
        # Create file menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label=QUIT_MENU, command=lambda: self.quit_application())
        # Add file menu to the menu bar
        self.menu_bar.add_cascade(label=FILE_MENU, menu=self.file_menu)
        # Set the menu bar for the root window
        self.root.config(menu=self.menu_bar)

        self.root.mainloop()
        
    def quit_application(self):
        if messagebox.askokcancel(MSG_QUIT_LABEL, QUIT_QUESTION):
            self.root.destroy()