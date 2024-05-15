import tkinter as tk
from tkinter import StringVar, filedialog, messagebox
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)

        # Ask the user to select a directory for saving the downloaded video
        download_folder = filedialog.askdirectory()
        if download_folder:  # If a folder is selected
            # Setting the download folder
            video = ytObject.streams.get_highest_resolution()
            video.download(download_folder)

            # Update UI elements
            title.configure(text=ytObject.title, text_color="grey")
            finishLabel.configure(text="Downloaded!")
        else:
            finishLabel.configure(text="Download canceled!", text_color="red")
    except Exception as e:
        finishLabel.configure(text="Download error!", text_color="red")
        messagebox.showerror("Error", str(e))


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# Our app frame
app = customtkinter.CTk()
app.geometry("1024x768")
app.title("Youtube Downloader")

# Culoarea background-ului


# Adding an image
image = Image.open(
    "C:\Proiecte Python\GUI project YT Downloader\Images\yt-logo2c.jpg")
photo = ImageTk.PhotoImage(image)
img_label = tk.Label(app, image=photo)
img_label.pack()

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
