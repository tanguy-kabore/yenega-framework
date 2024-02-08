from tkinter import messagebox, filedialog, simpledialog, ttk
from tkinter.font import Font
from stegano import lsb
import platform
import psutil
import socket
from src.widget import *

class Steganography:
    @staticmethod
    def hide_text_message():
            # Open a file dialog to select the cover image
            cover_image_path = filedialog.askopenfilename(title="Select Cover Image")

            if cover_image_path:
                # Get the text message from the user
                text_message = simpledialog.askstring("Hide Text", "Enter the text message to hide")

                if text_message:
                    try:
                        # Hide the text message within the cover image
                        stegano_image = lsb.hide(cover_image_path, text_message)
                        stegano_image.save(cover_image_path)  # Overwrite the cover image with the stegano image
                        messagebox.showinfo("Success", "Text message hidden successfully!")
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred while hiding the text message: {str(e)}")
                else:
                    messagebox.showwarning("Warning", "No text message provided.")
            else:
                messagebox.showwarning("Warning", "No cover image selected.")

    @staticmethod
    def extract_text_message():
        # Open a file dialog to select the stegano image
        stegano_image_path = filedialog.askopenfilename(title="Select Stegano Image")

        if stegano_image_path:
            try:
                # Extract the hidden text message from the stegano image
                text_message = lsb.reveal(stegano_image_path)
                if text_message:
                    messagebox.showinfo("Extracted Text", f"The hidden text message is:\n\n{text_message}")
                else:
                    messagebox.showinfo("Extracted Text", "No hidden text message found.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while extracting the text message: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No stegano image selected.")

    @staticmethod
    def clear_text_message():
        stegano_image_path = filedialog.askopenfilename(title="Select Stegano Image")
        
        if stegano_image_path:
            # Extract the hidden message from the stegano image
            hidden_message = lsb.reveal(stegano_image_path)

            # Overwrite the stegano image with the original cover image
            lsb.hide(stegano_image_path, hidden_message)

            messagebox.showinfo("Clear Message", "Message cleared successfully!")
        else:
            messagebox.showwarning("Warning", "No stegano image selected.")

    @staticmethod
    def check_steganography():
        stegano_image_path = filedialog.askopenfilename(title="Select Stegano Image")
        
        if stegano_image_path:
            try:
                message = lsb.reveal(stegano_image_path)
                messagebox.showinfo("Steganography Check", "The image contains a hidden message.")
            except:
                messagebox.showinfo("Steganography Check", "The image does not contain a hidden message.")
        else:
            messagebox.showwarning("Warning", "No stegano image selected.")

class Device():
    @staticmethod
    def device_info(root):
        frame = Frame(root, bg='white', bd=4)
        frame.grid_columnconfigure(0, weight=1)
        
        info_label = Label(frame, text='System information', bg='white', fg='black', font='Abnes 30 bold')
        info_label.grid(row=0, column=0, columnspan=2, sticky='we')
        
        labels = ['Operating System:', 'OS Version:', 'Processor:']
        info_texts = [platform.system(), platform.release(), platform.processor()]
        
        for row, (label_text, info_text) in enumerate(zip(labels, info_texts), start=1):
            label = Label(frame, text=label_text, bg='white', fg='black', font='Lato 15 bold')
            label.grid(row=row, column=0, sticky='e')
            
            info = Label(frame, text=info_text, bg='white', fg='black', font='Lato 15')
            info.grid(row=row, column=1, sticky='w')
            
            # Calculate text height
            label_font = Font(font=label['font'])
            info_font = Font(font=info['font'])
            label_text_height = label_font.metrics('linespace')
            info_text_height = info_font.metrics('linespace')
            
            # Set row height to the maximum of label and info text height
            max_text_height = max(label_text_height, info_text_height)
            frame.grid_rowconfigure(row, minsize=max_text_height)
        
        frame.grid()
        return frame

class Network:
    @staticmethod
    def network_info(root):
        frame = Widget.create_frame(root, 'white', 0, 2)  # Set initial rows to 0
        frame.grid_columnconfigure(0, weight=1)  # Configure column to resize proportionally
        frame.grid_rowconfigure(0, weight=1)  # Configure row to resize proportionally

        info_label = Widget.TextLabel(
            frame,
            'Network information',
            SECONDARY_COLOR,
            "Abnes 30 bold"
        )
        info_label.grid(row=0, column=0, columnspan=2, sticky='we')
        info_label.configure(bg=root['bg'])

        ip_addresses = psutil.net_if_addrs()
        row = 1  # Start with row 1 for data labels and info
        for interface, addresses in ip_addresses.items():
            for address in addresses:
                if address.family == socket.AF_INET:
                    # Add a horizontal line before each new block
                    line = ttk.Separator(frame, orient='horizontal')
                    line.grid(row=row, column=0, columnspan=2, sticky='ew')
                    row += 1
                    label1 = Widget.TextLabel(frame, 'Interface:', 'black', "Lato 15 bold")
                    label1.grid(row=row, column=0, sticky='e')
                    label1.configure(bg=root['bg'])
                    info1 = Widget.TextLabel(frame, interface, 'black', "Lato 15")
                    info1.grid(row=row, column=1, sticky='w')
                    info1.configure(bg=root['bg'])
                    row += 1

                    label2 = Widget.TextLabel(frame, 'IP Address:', 'black', "Lato 15 bold")
                    label2.grid(row=row, column=0, sticky='e')
                    label2.configure(bg=root['bg'])
                    info2 = Widget.TextLabel(frame, address.address, 'black', "Lato 15")
                    info2.grid(row=row, column=1, sticky='w')
                    info2.configure(bg=root['bg'])
                    row += 1

                    label3 = Widget.TextLabel(frame, 'Netmask:', 'black', "Lato 15 bold")
                    label3.grid(row=row, column=0, sticky='e')
                    label3.configure(bg=root['bg'])
                    info3 = Widget.TextLabel(frame, address.netmask, 'black', "Lato 15")
                    info3.grid(row=row, column=1, sticky='w')
                    info3.configure(bg=root['bg'])
                    row += 1

                    label4 = Widget.TextLabel(frame, 'Broadcast IP:', 'black', "Lato 15 bold")
                    label4.grid(row=row, column=0, sticky='e')
                    label4.configure(bg=root['bg'])
                    info4 = Widget.TextLabel(frame, address.broadcast, 'black', "Lato 15")
                    info4.grid(row=row, column=1, sticky='w')
                    info4.configure(bg=root['bg'])
                    row += 1

        # Update the number of rows in the frame
        frame.grid_rowconfigure(row, weight=1)

        return frame
