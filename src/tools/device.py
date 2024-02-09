from tkinter.font import Font
import platform
from src.widget import *

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