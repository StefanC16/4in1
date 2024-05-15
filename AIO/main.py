import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, StringVar
import requests
import subprocess
from tkinter import *
import os

import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk

import phonenumbers
from phonenumbers import geocoder, carrier


def login():
    # Function to handle login
    if username_entry.get() == 'admin' and password_entry.get() == 'admin':
        messagebox.showinfo(
            title="Login", message="You successfully logged in.")
        hide_widgets(frame_login)
        show_widgets(frame_menu)
    else:
        messagebox.showerror(title="Error", message="Invalid login.")


def hide_widgets(frame):
    frame.pack_forget()


def show_widgets(frame):
    frame.pack()


def open_converter():
    # Function to open currency converter
    subprocess.Popen(
        ["python", "AIO/Currency converter-/currency_converter.py"])


def open_cryptus():
    # Function to open the CRYPTUS Python file
    subprocess.Popen(["python", "AIO/CryptuS-/CryptuS.py"])


def open_YTConverter():
    subprocess.Popen(["python", "AIO/YT Downloader/YT-downloader.py"])


def open_phonenofinder():
    subprocess.Popen(["python", "AIO/Phone Number Finder/phonenofinder.py"])


window = tk.Tk()
window.title("Currency Converter")
window.geometry("850x600")
window.configure(bg='#333333')

frame_login = tk.Frame(window, bg='#333333')
frame_menu = tk.Frame(window, bg='#333333')

# Login Frame Widgets
login_label = tk.Label(frame_login, text="Login",
                       bg='#333333', fg="#FF7930", font=("Arial", 30))
username_label = tk.Label(frame_login, text="Username",
                          bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame_login, font=("Arial", 16))
password_entry = tk.Entry(frame_login, show="*", font=("Arial", 16))
password_label = tk.Label(frame_login, text="Password",
                          bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(frame_login, text="Login", bg="#FF7930",
                         fg="#FFFFFF", font=("Arial", 16), command=login)

# Menu Frame Widgets
menu_label = tk.Label(frame_menu, text="Menu", bg='#333333',
                      fg="#FF7930", font=("Arial", 30))
converter_button = tk.Button(frame_menu, text="Currency Converter",
                             bg="#FF7930", fg="#FFFFFF", font=("Arial", 16), command=open_converter)
cryptus_button = tk.Button(frame_menu, text="CryptuS", bg="#FF7930",
                           fg="#FFFFFF", font=("Arial", 16), command=open_cryptus)
yt_button = tk.Button(frame_menu, text="YouTube Downloader", bg="#FF7930",
                      fg="#FFFFFF", font=("Arial", 16), command=open_YTConverter)
phonenofinder_button = tk.Button(frame_menu, text="Phone Number Finder", bg="#FF7930",
                                 fg="#FFFFFF", font=("Arial", 16), command=open_phonenofinder)
exit_button = tk.Button(frame_menu, text="Exit", bg="#FF2433",
                        fg="#FFFFFF", font=("Arial", 16), command=window.destroy)

widgets_login = [
    login_label, username_label, username_entry,
    password_label, password_entry, login_button
]


# Grid for Login Frame Widgets
for widget in widgets_login:
    widget.grid(row=widgets_login.index(widget), column=0,
                columnspan=2, sticky="nsew", pady=20)

# Grid for Menu Frame Widgets
menu_label.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=40)
converter_button.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=20)
cryptus_button.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=20)
yt_button.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=20)
phonenofinder_button.grid(
    row=4, column=0, columnspan=2, sticky="nsew", pady=20)
exit_button.grid(
    row=5, column=0, columnspan=2, sticky="nsew", pady=20)

frame_login.pack()

window.mainloop()
