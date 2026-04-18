import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder="music"):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.is_paused = False
        self._load_playlist()

    def _load_playlist(self):
        supported = (".wav", ".mp3", ".ogg")
     
        if not os.path.exists(self.music_folder):
            print(f"Ошибка: Папка {self.music_folder} не найдена!")
            return
        
        files = sorted(os.listdir(self.music_folder))
        for f in files:
            if f.lower().endswith(supported):
                self.playlist.append(os.path.join(self.music_folder, f))

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            self.is_playing = True
            self.is_paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False

    def pause_resume(self):
        if self.is_playing:
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
            else:
                pygame.mixer.music.pause()
                self.is_paused = True

    def next_track(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play()

    def prev_track(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play()

    def update(self):
        if self.is_playing and not self.is_paused and not pygame.mixer.music.get_busy():
            self.next_track()

    def get_track_name(self):
        if not self.playlist: return "Нет треков"
        return os.path.basename(self.playlist[self.current_index])

    def get_status(self):
        if not self.is_playing and not self.is_paused: return "⏹ Стоп"
        return "⏸ Пауза" if self.is_paused else "▶ Играет"

    def get_position_seconds(self):
        if self.is_playing or self.is_paused:
            return pygame.mixer.music.get_pos() // 1000
        return 0

    def get_total_tracks(self):
        return len(self.playlist)
