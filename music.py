import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player with Visualizer")
        self.root.geometry("500x300")

        self.current_dir = os.getcwd()

        self.playlist = []

        self.initialize_player()
        self.initialize_visualizer()

    def initialize_player(self):
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.add_button = tk.Button(self.root, text="Add Music", command=self.add_music)
        self.add_button.pack()

        self.playlist_box = tk.Listbox(self.root)
        self.playlist_box.pack()

    def initialize_visualizer(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.screen = pygame.display.set_mode((500, 300))
        pygame.display.set_caption("Music Visualizer")

        self.running = True

    def play_music(self):
        pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def add_music(self):
        file_path = filedialog.askopenfilename(initialdir=self.current_dir, title="Select Music", filetypes=(("Audio Files", "*.mp3"), ("All Files", "*.*")))
        if file_path:
            self.playlist.append(file_path)
            self.playlist_box.insert(tk.END, os.path.basename(file_path))

    def run_visualizer(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))

            # Insert visualization code here

            pygame.display.flip(
            self.clock.tick(self.fps)
        pygame.quit()
if __name__ == "_main__":
    root = tk.Tk(
    music_player = MusicPlayer(oot)
    music_player.run_visualizer(