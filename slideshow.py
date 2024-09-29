from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk


root = tk.Tk()
root.title("Image Slideshow Viewer")

image_paths = [
    r"C:\Users\meetp\OneDrive\Pictures\bappa.jpg",
    r"C:\Users\meetp\OneDrive\Pictures\profileimage.png",
    r"C:\Users\meetp\OneDrive\Pictures\boy.png",
    r"C:\Users\meetp\OneDrive\Pictures\JSF_8488-01.jpeg.jpg",
    r"C:\Users\meetp\OneDrive\Pictures\1.jpg"
]


image_size=(1080,1080)
images=[Image.open(path). resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)


slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
