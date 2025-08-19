import pygame
from music_library import music_files

class MusicPlayer:
    def __init__(self, music_files):
        pygame.mixer.init()
        self.music_files = music_files
        self.current_index = 0
        self.is_playing = False
        self.volume = 0.5  # Default volume (50%)
        pygame.mixer.music.set_volume(self.volume)

    def play_song(self):
        pygame.mixer.music.load(self.music_files[self.current_index])
        pygame.mixer.music.play()
        self.is_playing = True
        print(f"Playing: {self.music_files[self.current_index]}")

    def pause_song(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            print("Paused")

    def resume_song(self):
        if not self.is_playing:
            pygame.mixer.music.unpause()
            self.is_playing = True
            print("Resumed")

    def next_song(self):
        self.current_index = (self.current_index + 1) % len(self.music_files)
        self.play_song()

    def previous_song(self):
        self.current_index = (self.current_index - 1) % len(self.music_files)
        self.play_song()

    def volume_up(self):
        self.volume = min(self.volume + 0.1, 1.0)  # Cap the volume at 1.0
        pygame.mixer.music.set_volume(self.volume)
        print(f"Volume increased to: {int(self.volume * 100)}%")

    def volume_down(self):
        self.volume = max(self.volume - 0.1, 0.0)  # Lower limit is 0.0
        pygame.mixer.music.set_volume(self.volume)
        print(f"Volume decreased to: {int(self.volume * 100)}%")

    def stop_song(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        print("Stopped")


def execute_command(player, command):
    """
    Executes a command on the given MusicPlayer instance.

    :param player: An instance of MusicPlayer
    :param command: The command to execute as a string
    """
    if command == "play":
        player.play_song()
    elif command == "pause":
        player.pause_song()
    elif command == "resume":
        player.resume_song()
    elif command == "next":
        player.next_song()
    elif command == "previous":
        player.previous_song()
    elif command == "volume_up":
        player.volume_up()
    elif command == "volume_down":
        player.volume_down()
    elif command == "stop":
        player.stop_song()
    else:
        print("Invalid command.")
