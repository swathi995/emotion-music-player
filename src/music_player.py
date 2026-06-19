import random
import os
import pygame

pygame.init()
pygame.mixer.init()

last_emotion = None

def play_music(emotion):
    global last_emotion

    if emotion == last_emotion:
        return

    last_emotion = emotion

    folder = os.path.join("assets/songs", emotion)

    if not os.path.exists(folder):
        print("Folder missing:", folder)
        return

    songs = [f for f in os.listdir(folder) if f.endswith(".mp3")]

    if len(songs) == 0:
        print("No songs in:", folder)
        return

    song = random.choice(songs)
    song_path = os.path.join(folder, song)

    print("Playing:", song_path)

    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()