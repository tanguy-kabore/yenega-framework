import os
from tkinter import messagebox, filedialog, simpledialog
from stegano import lsb
import logging

# Assuming you have configured the logging as mentioned before
logger = logging.getLogger()

class Steganography:
    @staticmethod
    def hide_text_message():
        # Ouvrir une boîte de dialogue pour sélectionner l'image de couverture
        cover_image_path = filedialog.askopenfilename(title="Select Cover Image")

        if cover_image_path:
            # Obtenir le message texte de l'utilisateur
            text_message = simpledialog.askstring("Hide Text", "Enter the text message to hide")

            if text_message:
                try:
                    # Cacher le message texte dans l'image de couverture
                    stegano_image = lsb.hide(cover_image_path, text_message)
                    
                    # Obtenir le chemin de l'image stégano
                    stegano_image_path = os.path.splitext(cover_image_path)[0] + "_stegano.png"
                    
                    stegano_image.save(stegano_image_path)  # Enregistrer l'image stégano
                    messagebox.showinfo("Success", f"Text message hidden successfully! Stégano image saved at {stegano_image_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while hiding the text message: {str(e)}")
                    print(f"Steganography Error: {str(e)}")
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
                
                if text_message is not None:
                    messagebox.showinfo("Extracted Text", f"The hidden text message is:\n\n{text_message}")
                else:
                    messagebox.showinfo("Extracted Text", "No hidden text message found.")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
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
                revealed_message = lsb.reveal(stegano_image_path)
                
                if revealed_message:
                    messagebox.showinfo("Steganography Check", "The image contains a hidden message.")
                    logger.info("Image contains a hidden message: %s", stegano_image_path)
                else:
                    messagebox.showinfo("Steganography Check", "The image does not contain a hidden message.")
                    logger.info("Image does not contain a hidden message: %s", stegano_image_path)

            except IndexError as e:
                messagebox.showinfo("Steganography Check", "Impossible to detect message.")
                logger.info("Impossible to detect message in %s: %s", stegano_image_path, str(e))
        else:
            messagebox.showwarning("Warning", "No stegano image selected.")
            logger.warning("No stegano image selected for steganography check.")