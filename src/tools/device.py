from tkinter import Frame, Label, N, E, W, S, CENTER
import platform
from src.widget import *

class Device():
    @staticmethod
    def device_info(root):
        frame = Frame(root, bg='white', bd=4)
        frame.grid_columnconfigure(0, weight=0)  # Permet à la colonne de s'étendre

        info_label = Label(frame, text='System information', bg='white', fg='black', font='Abnes 30 bold')
        info_label.grid(row=0, column=0, columnspan=2, sticky='nsew')  # Utilise sticky pour l'ancrer au nord

        labels = ['Operating System:', 'OS Version:', 'Processor:']
        info_texts = [platform.system(), platform.release(), platform.processor()]

        for row, (label_text, info_text) in enumerate(zip(labels, info_texts), start=1):
            label = Label(frame, text=label_text, bg='white', fg='black', font='Lato 15 bold')
            label.grid(row=row, column=0, sticky='e')  # Utilise sticky pour l'ancrer à l'est

            info = Label(frame, text=info_text, bg='white', fg='black', font='Lato 15')
            info.grid(row=row, column=1, sticky='w')  # Utilise sticky pour l'ancrer à l'ouest

        frame.pack(fill='both', expand=True)

        return frame