from tkinter import Frame, Label, N, E, W, S, CENTER, ttk
import platform
import psutil
from src.widget import *

class Device:
    @staticmethod
    def device_info(root):
        frame = Frame(root, bg='white', bd=4)
        frame.grid_columnconfigure(0, weight=1)  # Permet à la colonne de s'étendre

        info_label = Label(frame, text='System information', bg='white', fg='black', font='Abnes 20 bold')
        info_label.grid(row=0, column=0, columnspan=2, sticky='nsew')  # Utilise sticky pour l'ancrer au nord

        labels = ['Operating System:', 'OS Version:', 'Processor:']
        info_texts = [platform.system(), platform.release(), platform.processor()]

        for row, (label_text, info_text) in enumerate(zip(labels, info_texts), start=1):
            label = Label(frame, text=label_text, bg='white', fg='black', font='Lato 15 bold')
            label.grid(row=row, column=0, sticky='e')  # Utilise sticky pour l'ancrer à l'est

            info = Label(frame, text=info_text, bg='white', fg='black', font='Lato 15')
            info.grid(row=row, column=1, sticky='w')  # Utilise sticky pour l'ancrer à l'ouest

        # Ajouter un séparateur
        separator1 = ttk.Separator(frame, orient='horizontal')
        separator1.grid(row=row + 1, column=0, columnspan=2, sticky='ew')
        row += 2

        # Ajouter des informations sur la mémoire RAM
        ram_label = Label(frame, text='RAM information', bg='white', fg='black', font='Abnes 20 bold')
        ram_label.grid(row=row, column=0, columnspan=2, sticky='nsew')  
        row += 1

        ram_info_labels = ['Total RAM:', 'Available RAM:', 'Used RAM:']
        ram_info_values = [psutil.virtual_memory().total, psutil.virtual_memory().available, psutil.virtual_memory().used]

        for label_text, info_value in zip(ram_info_labels, ram_info_values):
            label = Label(frame, text=label_text, bg='white', fg='black', font='Lato 15 bold')
            label.grid(row=row, column=0, sticky='e')  

            info = Label(frame, text=f'{info_value / (1024 ** 3):.2f} GB', bg='white', fg='black', font='Lato 15')
            info.grid(row=row, column=1, sticky='w')  
            row += 1

        # Ajouter un séparateur
        separator2 = ttk.Separator(frame, orient='horizontal')
        separator2.grid(row=row, column=0, columnspan=2, sticky='ew')
        row += 1

        # Ajouter des informations sur le disque dur
        disk_label = Label(frame, text='Disk information', bg='white', fg='black', font='Abnes 20 bold')
        disk_label.grid(row=row, column=0, columnspan=2, sticky='nsew')  
        row += 1

        disk_info_labels = ['Total Disk Space:', 'Free Disk Space:', 'Used Disk Space:']
        disk_info_values = [psutil.disk_usage('/').total, psutil.disk_usage('/').free, psutil.disk_usage('/').used]

        for label_text, info_value in zip(disk_info_labels, disk_info_values):
            label = Label(frame, text=label_text, bg='white', fg='black', font='Lato 15 bold')
            label.grid(row=row, column=0, sticky='e')  

            info = Label(frame, text=f'{info_value / (1024 ** 3):.2f} GB', bg='white', fg='black', font='Lato 15')
            info.grid(row=row, column=1, sticky='w')  
            row += 1

        frame.pack(fill='both', expand=True)

        return frame