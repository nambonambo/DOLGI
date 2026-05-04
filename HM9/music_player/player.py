import pygame
import os

playlist = []
index = 0
is_playing = False

def init_player(music_folder):
    global playlist, index, is_playing
    pygame.mixer.init()

    playlist = load_music(music_folder)
    index = 0
    is_playing = False


def load_music(music_folder):
    files = []
    for file in os.listdir(music_folder):
        if file.endswith(".mp3") or file.endswith(".wav"):
            files.append(os.path.join(music_folder, file))
    return files


def play():
    global is_playing

    if not playlist:
        return

    track = playlist[index]
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()
    is_playing = True


def stop():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False


def next_track():
    global index
    if not playlist:
        return

    index = (index + 1) % len(playlist)
    play()


def prev_track():
    global index
    if not playlist:
        return

    index = (index - 1) % len(playlist)
    play()


def get_current_track_name():
    if not playlist:
        return "No music"

    return os.path.basename(playlist[index])


def get_status():
    return "Playing" if is_playing else "Stopped"