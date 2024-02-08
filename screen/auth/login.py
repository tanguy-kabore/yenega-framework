import os
from tkinter import Label, BooleanVar, Checkbutton
from PIL import Image, ImageTk
from env import *
from src.widget import Widget
from src.auth import Auth
from translation import *
from screen.home import HomeScreen 

class LoginScreen:
    def __init__(self):
        self.root = Widget.Screen(0.5, 6, 3, False)
        self.checkbox_var = BooleanVar()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Navigate up two directories to reach the project directory
        project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
        image = Image.open(project_dir+LOGO_PNG).convert('RGBA')
        width, height = image.size
        aspect_ratio = width / height
        new_width = width // 3  # Adjust as needed, same as the number of row
        new_height = int(new_width / aspect_ratio)
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        # Create a label to display the image
        image_label = Label(self.root, image=photo)
        image_label.configure(bg=self.root['bg'])  # Set the label background to transparent
        image_label.image = photo  # Store a reference to avoid garbage collection
        image_label.grid(row=0, column=1, sticky="nsew")

        self.form_label = Widget.TextLabel(
            self.root, 
            LOGIN_HEAD, 
            SECONDARY_COLOR, 
            "Abnes 30 bold")
        self.form_label.grid(row=1, column=1)
        self.form_label.configure(bg=self.root['bg'])

        self.label_status = Widget.TextLabel(
            self.root,
            '',
            SECONDARY_COLOR, 
            "Lato 15 bold")
        self.label_status.grid(row=2, column=1)
        self.label_status.configure(bg=self.root['bg'])

        self.username_label = Widget.TextLabel(
            self.root, 
            USERNAME_LABEL, 
            SECONDARY_COLOR, 
            "Lato 15 bold")
        self.username_label.grid(row=3, column=0, sticky="w", padx=(30, 0)) # Align to the left and apply padx only to the left side
        self.username_label.configure(bg=self.root['bg'])
        self.username_label.configure(bg=self.root['bg'])
        self.username_entry = Widget.TextEntry(
            self.root, 
            SECONDARY_COLOR, 
            "Lato 15", 
            "text")
        self.username_entry.grid(row=3, column=1, sticky="ew")

        self.password_label = Widget.TextLabel(
            self.root, 
            PASSWORD_LABEL, 
            SECONDARY_COLOR, 
            "Lato 15 bold")
        self.password_label.grid(row=4, column=0, sticky="w", padx=(30, 0))
        self.password_label.configure(bg=self.root['bg'])
        self.password_entry = Widget.TextEntry(
            self.root, 
            SECONDARY_COLOR, 
            "Lato 15", 
            "password")
        self.password_entry.grid(row=4, column=1, sticky="ew")
        self.check_button = Checkbutton(
            self.root, 
            text=SHOW_PASSWORD_LABEL, 
            font=("Lato 10"), 
            variable=self.checkbox_var,
            command=self.on_checkbox_toggle(), )
        self.check_button.grid(row=4, column= 2)
        self.check_button.configure(bg=self.root['bg'])
            
        self.login_button = Widget.TextButton(
            self.root, 
            SUBMIT_LABEL, 
            "Lato 15 bold")
        self.login_button.grid(row=5, column= 1, sticky="ew", pady=10)
        # Assign the command to the button after it is created
        self.login_button.config(command=self.login_button_clicked)
        self.root.grid_columnconfigure(1, weight=1)  # Set column weight to occupy the width
        # Bind the <Return> event to the login button handler
        self.root.bind('<Return>', self.login_button_clicked)
        self.root.mainloop()

    def on_checkbox_toggle(self, event=None):
        def wrapper():
            if self.checkbox_var.get():
                self.password_entry.config(show='')
            else:
                self.password_entry.config(show='*')
        return wrapper
    
    def login_button_clicked(self, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()
        status = Auth.validate_login(username, password)  # Perform login validation with retrieved values
        if status == True:
            self.root.destroy()  # Close the login window
            HomeScreen('admin')
        else:
            
            self.label_status.config(text=USER_NOT_FOUND+" "+OR+" "+INCORRECT_PASSWORD, fg='red')