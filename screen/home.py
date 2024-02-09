from tkinter import *
from tkinter import messagebox
from src.widget import Widget
from translation import *
from src.tools.device import Device
from src.tools.network import Network
from src.tools.steganography import Steganography

class HomeScreen:
    def __init__(self, user_info):
        self.root = Widget.Screen(1, 1, 1, True)
        self.user_info = user_info
        self.current_frame = None
        self.create_menu_bar()
        self.create_welcome_label()
        self.root.mainloop()

    def create_menu_bar(self):
        self.menu_bar = Menu(self.root)
        self.create_file_menu()
        if self.user_info == "admin":
            self.create_tool_menu()
        self.root.config(menu=self.menu_bar)
    
    def create_welcome_label(self):
        # Create a label widget for the welcome message
        welcome_label = Label(self.root, text="Welcome to the world of Ethical Hacking", font=("Abnes", 20, "bold"))

        # Center the label in the window
        welcome_label.pack(expand=True)
        welcome_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def create_file_menu(self):
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label=QUIT_MENU, command=self.quit_application)
        self.menu_bar.add_cascade(label=FILE_MENU, menu=self.file_menu)

    def create_tool_menu(self):
        self.tool_menu = Menu(self.menu_bar, tearoff=0)
        self.tool_menu.add_command(label='Device', command=lambda: self.create_frame('Device'))
        self.tool_menu.add_command(label='Network', command=lambda: self.create_frame('Network'))
        self.create_steganography_submenu()
        self.menu_bar.add_cascade(label="Tools", menu=self.tool_menu)

    def create_steganography_submenu(self):
        self.steganography_menu = Menu(self.tool_menu, tearoff=0)
        self.steganography_menu.add_command(label='Hide Text', command=self.hide_text_message)
        self.steganography_menu.add_command(label='Extract Text', command=self.extract_text_message)
        # self.steganography_menu.add_command(label='Clear Text', command=self.clear_text_message)
        # self.steganography_menu.add_command(label='Steganography ?', command=self.check_steganography)
        self.tool_menu.add_cascade(label='Steganography', menu=self.steganography_menu)

    def hide_text_message(self):
        Steganography.hide_text_message()  # Call the function from stegano_utils.py
    
    def extract_text_message(self):
        Steganography.extract_text_message()

    def clear_text_message(self):
        Steganography.clear_text_message()
    
    def check_steganography(self):
        Steganography.check_steganography()

    def quit_application(self):
        if messagebox.askokcancel(MSG_QUIT_LABEL, QUIT_QUESTION):
            self.root.destroy()

    def create_frame(self, frame_name):
        self.close_current_frame()
        if frame_name == 'Device':
            new_frame = Device.device_info(self.root)
        elif frame_name == 'Network':
            new_frame = Network.network_info(self.root)
        else:
            # Handle unknown frame names
            messagebox.showerror("Error", "Unknown frame name: {}".format(frame_name))
            return
        self.current_frame = new_frame

    def close_current_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None