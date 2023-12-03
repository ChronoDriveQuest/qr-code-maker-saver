import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import os
import string  # Import the string module

# Function to create a valid filename from text
def sanitize_filename(text):
    # Replace spaces with underscores and remove any non-alphanumeric characters except for a few special characters
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized = ''.join(c for c in text if c in valid_chars)
    return sanitized.replace(' ', '_')

# Function to create a QR code with alphanumeric content and save a text file
def create_qr_code(alphanumeric_text, folder='QR_codes'):
    sanitized_text = sanitize_filename(alphanumeric_text)
    qr_filename = f'{sanitized_text}_qr.png'
    text_filename = f'{sanitized_text}_text.txt'

    # Create the folder if it does not exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Full paths for the files
    qr_file_path = os.path.join(folder, qr_filename)
    text_file_path = os.path.join(folder, text_filename)

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(alphanumeric_text)
    qr.make(fit=True)

    # Save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_file_path)

    # Save the text
    with open(text_file_path, 'w') as file:
        file.write(alphanumeric_text)

    return qr_file_path, text_file_path

# Function to update the QR code display and bind click event
def update_qr_display(filename, data):
    img = Image.open(filename)
    img = img.resize((250, 250), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.photo = img  # keep a reference
    qr_label.bind('<Button-1>', lambda e: show_text(data))  # Bind click event

# Function to show text on QR code click
def show_text(data):
    messagebox.showinfo("Drive Quest", data)

# Function to handle the submit action
def on_submit():
    text = text_entry.get()
    if not re.match("^[a-zA-Z0-9\s\.\,\:\;\!\?\-]+$", text):
        messagebox.showerror("Error", "Only alphanumeric characters, spaces, and .,:;!?- are allowed.")
        return
    try:
        qr_filename, text_filename = create_qr_code(text)  # Capture both filenames
        update_qr_display(qr_filename, text)  # Update display with the QR code filename
    except Exception as e:
        messagebox.showerror("Error", str(e))
        print("Error:", e)  # Print the error for debugging

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")

text_entry = tk.Entry(root, width=50)
text_entry.pack()

submit_btn = tk.Button(root, text="Drive Quest", command=on_submit)
submit_btn.pack()

qr_label = tk.Label(root)
qr_label.pack()

root.mainloop()
