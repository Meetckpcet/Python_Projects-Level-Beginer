import tkinter as tk
from tkinter import Entry, Button, Label
import webbrowser

root =tk.Tk()
root.title("Your AI Assistant")

root.config(bg='steelblue')

def search_youtube():
    query=entry.get()
    url=f'https://www.youtube.com/results?search_query={query}'
    webbrowser.open(url)

def search_google():
    query=entry.get()
    url=f'https://www.google.com/search?q={query}'
    webbrowser.open(url)

def search_instagram():
    Username=entry.get().replace("@","")
    url=f'www.instagram.com/{Username}/'
    webbrowser.open(url)

Label(root, text="Enter Your Command:").pack(pady=10)
entry=Entry(root, width=50)
entry.pack(pady=10)

Button(root, text="Search On Youtube", command=search_youtube).pack(pady=5)
Button(root, text="Search On Google", command=search_google).pack(pady=5)
Button(root, text="Search On Instagram", command=search_instagram).pack(pady=5)

root.mainloop()