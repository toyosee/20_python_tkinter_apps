import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os

root = tk.Tk()
root.title("Personal Music Player")
root.geometry("400x300")

# Initialize mixer
mixer.init()

playlist = []
current_song_index = 0

def add_to_playlist():
    files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
    for file in files:
        playlist.append(file)
    update_playlist_box()

def update_playlist_box():
    playlist_box.delete(0, tk.END)
    for song in playlist:
        playlist_box.insert(tk.END, os.path.basename(song))

def play_song():
    global current_song_index
    if playlist:
        mixer.music.load(playlist[current_song_index])
        mixer.music.play()

def pause_song():
    mixer.music.pause()

def stop_song():
    mixer.music.stop()

def resume_song():
    mixer.music.unpause()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play_song()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    play_song()

def set_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

# Control buttons
control_frame = tk.Frame(root)
control_frame.pack(pady=20)

play_button = tk.Button(control_frame, text="Play", command=play_song)
play_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(control_frame, text="Pause", command=pause_song)
pause_button.grid(row=0, column=1, padx=5)

stop_button = tk.Button(control_frame, text="Stop", command=stop_song)
stop_button.grid(row=0, column=2, padx=5)

resume_button = tk.Button(control_frame, text="Resume", command=resume_song)
resume_button.grid(row=0, column=3, padx=5)

prev_button = tk.Button(control_frame, text="Previous", command=prev_song)
prev_button.grid(row=1, column=0, padx=5)

next_button = tk.Button(control_frame, text="Next", command=next_song)
next_button.grid(row=1, column=1, padx=5)

# Volume control
volume_slider = tk.Scale(control_frame, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume", command=set_volume)
volume_slider.set(70)
volume_slider.grid(row=1, column=2, columnspan=2)

# Playlist box
playlist_box = tk.Listbox(root)
playlist_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add to Playlist", command=add_to_playlist)
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
