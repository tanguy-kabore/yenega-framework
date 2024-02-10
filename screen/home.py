from tkinter import *
from tkinter import Toplevel, Label, Frame
from tkinter import messagebox, filedialog
from src.widget import Widget
from src.tools.device import Device
from src.tools.network import Network
from src.tools.steganography import Steganography
from src.tools.antivirus import AntivirusScanner

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
            self.create_antivirus_menu()  # Add antivirus menu for admin
        self.root.config(menu=self.menu_bar)

    def create_welcome_label(self):
        self.white_frame = Frame(self.root, bg='white')
        self.white_frame.pack(fill='both', expand=True)

        self.welcome_label = Label(
            self.white_frame,
            text="Welcome to the world of Ethical Hacking",
            font=("Abnes", 20, "bold"),
            bg='white'
        )
        self.welcome_label.pack(expand=True)
        self.welcome_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def create_file_menu(self):
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Quit", command=self.quit_application)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

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
        self.tool_menu.add_cascade(label='Steganography', menu=self.steganography_menu)

    def create_antivirus_menu(self):
        self.antivirus_menu = Menu(self.menu_bar, tearoff=0)
        self.antivirus_menu.add_command(label='Scan', command=self.scan_antivirus)
        self.menu_bar.add_cascade(label="Antivirus", menu=self.antivirus_menu)

    def hide_text_message(self):
        Steganography.hide_text_message()

    def extract_text_message(self):
        Steganography.extract_text_message()

    def quit_application(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def create_frame(self, frame_name):
        self.close_current_frame()

        if frame_name == 'Device':
            DeviceWindow(self.root)
        elif frame_name == 'Network':
            NetworkWindow(self.root)
        else:
            messagebox.showerror("Error", f"Unknown frame name: {frame_name}")

    def close_welcome_label(self):
        if self.white_frame is not None:
            self.white_frame.destroy()

    def close_current_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

    def scan_antivirus(self):
        file_path = filedialog.askopenfilename(
            title="Select File for Antivirus Scan",
            filetypes=[("All Files", "*.*")]
        )
        if file_path:
            result = self.perform_antivirus_scan(file_path)
            self.show_antivirus_scan_result(result, file_path)

    @staticmethod
    def perform_antivirus_scan(file_path):
        return AntivirusScanner.perform_scan(file_path)

    def show_antivirus_scan_result(self, result, file_path):
        messagebox.showinfo("Antivirus Scan Result", f"Scan Result for {file_path}:\n\n{result}")

class DeviceWindow(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('Device')
        self.configure_resizable()
        self.center_window()
        device_frame = Device.device_info(self)
        device_frame.pack(fill='both', expand=True, padx=10, pady=10)

    def configure_resizable(self):
        self.resizable(True, True)  # Permet de redimensionner la fenêtre

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width_percent = 0.75
        height_percent = 0.75

        width = int(screen_width * width_percent)
        height = int(screen_height * height_percent)

        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2

        self.geometry("{}x{}+{}+{}".format(width, height, x_position, y_position))


class NetworkWindow(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('Network')
        self.configure_resizable()
        self.center_window()
        network_frame = Network.network_info(self)
        network_frame.pack(fill='both', expand=True, padx=10, pady=10)

    def configure_resizable(self):
        self.resizable(True, True)  # Permet de redimensionner la fenêtre

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        width_percent = 0.75
        height_percent = 0.75

        width = int(screen_width * width_percent)
        height = int(screen_height * height_percent)

        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2

        self.geometry("{}x{}+{}+{}".format(width, height, x_position, y_position))

# Run the application
if __name__ == "__main__":
    user_info = "admin"  # Replace with actual user info
    app = HomeScreen(user_info)