from tkinter import  ttk
import psutil
import socket
from src.widget import *

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
