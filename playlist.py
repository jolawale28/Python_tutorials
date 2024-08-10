# Objective: Create a class to manage a music playlist.
# Description: Define a class Playlist with attributes name and songs (a list of song titles).
# Include methods add_song(title), remove_song(title), and list_songs() to manage the
# playlist.
# Task: Create an instance of the Playlist class, add and remove songs, and display the
# current playlist.

class Playlist:

    songs = ["Umbrella", "I'm alive!", "Hero"]

    def __init__(self, name, songs = []) -> None:
        self.name = name
        self.songs = songs
    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, name):
        if (name not in self.songs):
            print(f"{name} is not in the list of songs!")
            return
        
        for song in self.songs:
            if song == name:
                self.songs.remove(name)
    
    def list_songs(self):
        print(f"Songs in playlist '{self.name}' ({len(self.songs)} found!):")
        print("-" * 30)
        for song in self.songs:
            print(f"Name: {song}")

if __name__ == "__main__":
    playlist = Playlist("Motivation Songs", [
        "I'm Alive by Celine Dion",
        "Power of Love by Celine Dion ft R. Kelly",
        "Omo mi by Christy Essien Igbokwe"
    ])

    playlist.add_song("I'm unavailable by Davido")
    playlist.list_songs()
    playlist.remove_song("I'm Alive by Celine Dion")
    playlist.list_songs()