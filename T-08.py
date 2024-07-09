import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = []
        self.current_track_index = 0

    def load_playlist(self, playlist):
        self.playlist = playlist

    def play_music(self):
        if self.playlist:
            track = self.playlist[self.current_track_index]
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()
            print(f"Playing: {os.path.basename(track)}")

    def stop_music(self):
        pygame.mixer.music.stop()
        print("Music stopped.")

    def next_track(self):
        if self.playlist:
            self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
            self.play_music()

    def previous_track(self):
        if self.playlist:
            self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
            self.play_music()

def main():
    music_player = MusicPlayer()
    
    while True:
        print("\nMusic Player Menu")
        print("1. Add Track to Playlist")
        print("2. Play Music")
        print("3. Stop Music")
        print("4. Next Track")
        print("5. Previous Track")
        print("6. Show Playlist")
        print("7. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6/7): ").strip()
        
        if choice == '1':
            track_path = input("Enter the path to the MP3 file: ").strip()
            if os.path.exists(track_path) and track_path.endswith(".mp3"):
                music_player.playlist.append(track_path)
                print(f"Track '{os.path.basename(track_path)}' added to the playlist.")
            else:
                print("Invalid file path or file type. Please enter a valid MP3 file path.")
        
        elif choice == '2':
            music_player.play_music()
        
        elif choice == '3':
            music_player.stop_music()
        
        elif choice == '4':
            music_player.next_track()
        
        elif choice == '5':
            music_player.previous_track()
        
        elif choice == '6':
            if not music_player.playlist:
                print("No tracks in the playlist.")
            else:
                print("Playlist:")
                for index, track in enumerate(music_player.playlist):
                    print(f"{index + 1}. {os.path.basename(track)}")
        
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    main()
