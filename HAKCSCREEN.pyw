# WARNING PRESS F6 TO EXIT HACKSCREEN
# WARNING PRESS F6 TO EXIT HACKSCREEN
# WARNING PRESS F6 TO EXIT HACKSCREEN
# WARNING PRESS F6 TO EXIT HACKSCREEN





import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

def disable_event():
    pass

def exit_app(event=None):
    root.destroy()

# Create the window
root = tk.Tk()
root.title("You Have Been Hacked")
root.geometry("1920x1080")
root.configure(bg='white')

# Load and display the image
image_path = r"C:\Users\Lucas\Downloads\th.jpg"

try:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    image = Image.open(image_path)
    image = image.resize((1920, 1080))
    photo = ImageTk.PhotoImage(image)

    root.image = photo  # Prevent garbage collection

    label = tk.Label(root, image=photo)
    label.place(relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading image: {e}")
    tk.Label(root, text=f"Failed to load image:\n{e}", bg='white', fg='red', font=("Arial", 20)).pack(expand=True)

root.attributes('-fullscreen', True)
root.protocol("WM_DELETE_WINDOW", disable_event)
root.bind("<Escape>", disable_event)
root.bind("<F6>", exit_app)

root.mainloop()

