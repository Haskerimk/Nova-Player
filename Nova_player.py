## Note: for legal reasons im not including songs, get your own files, place them in the Music folder
# Also this was supposed to be a Tkinter app but i fucking hate tkinter what a piece of shit library

import os
from pygame import mixer
import math
music_files = []
folder = "Music"

def Play(selected_song):
        Song = mixer.Sound(folder + "/" + music_files[int(selected_song)]) ##Loads and plays the music
        mixer.Sound.play(Song)
def Pause():
    mixer.pause()
def Select():
    selected = input("Select Song\n")
    if selected.isdigit(): #Checks if its a digit so it can be used when selecting the song in that list
        Play(selected)
        ## Options while the song is playing
        while True:
            Options = input("[R]eplay - [Q]uit - [P]ause - [C]hange\n")
            match Options:
                case "R":
                    Play(selected)
                case "Q":
                    exit()
                case "P":
                    Pause()
                case "C":
                    Select()


def Reload():
    music_files.clear()
    for file in os.listdir(folder):
        music_files.append(file)
        print(music_files.index(file), ": ", file) #Reloads and refreshes the music list by rescanning the folder
        if len(music_files) <= 0:
            Select()
        else:
            print("No music found") ##if no songs it'll quit ## Note 22.11.2025, for some reason this doesn't work and the player quits right away if there are no songs found lmao
            quit()

def Run():
    try:
        mixer.init() #Initializes the audio mixer
    except:
        print("Mixer initialization failed")
        return
    if not os.path.isdir(folder):
        print("Folder doesn't exist")
    else:
        print(" * * * * * Nova Player * * * * *")
        Reload()

Run()

