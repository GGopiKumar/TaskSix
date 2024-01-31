"""
Author : G Gopi Kumar
Date : 31/01/2024

Program 3 :  Visit the URL https://github.com/rysp/typescript-oops/blob/master/Practice/music-player.md 
convert the UML diagram into Python Class and Methods

Logic : After going through the details in the URL below is the UML diagram
+--------------------------+
|      MusicPlayer         |
+--------------------------+
| - playlists: List[Playlist] |
| - audio_files: List[AudioFile] |
+--------------------------+
| + create_playlist(name: str, genre: str): Playlist |
| + add_audio_to_playlist(audio: AudioFile, playlist: Playlist): bool |
| + search_audio_by_name(name: str): AudioFile |
| + search_playlist_by_name(name: str): Playlist |
| + calculate_average_rating(): float |
| + customize_player(theme: str): bool |
+--------------------------+
"""
class MusicPlayer:
    def __init__(self):
        """
        Constructor to initialize the MusicPlayer object.
        """
        self.playlists = []  # List to store instances of Playlist
        self.audio_files = []  # List to store instances of AudioFile

    def create_playlist(self, name, genre):
        """
        Creates a new playlist with the given name and genre.

        Parameters:
        - name (str): Name of the playlist.
        - genre (str): Genre of the playlist.

        Returns:
        - Playlist: The created playlist.
        """
        playlist = playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def add_audio_to_playlist(self, audio, playlist):
        """
        Adds an audio file to a playlist.

        Parameters:
        - audio (AudioFile): The audio file to be added.
        - playlist (Playlist): The playlist to which the audio will be added.

        Returns:
        - bool: True if the addition is successful, False otherwise.
        """
        if playlist.add_audio(audio):
            return True
        else:
            return False

    def search_audio_by_name(self, name):
        """
        Searches for an audio file by name.

        Parameters:
        - name (str): The name of the audio file to search.

        Returns:
        - AudioFile: The found audio file or None if not found.
        """
        for audio in self.audio_files:
            if audio.get_name() == name:
                return audio
        return None

    def search_playlist_by_name(self, name):
        """
        Searches for a playlist by name.

        Parameters:
        - name (str): The name of the playlist to search.

        Returns:
        - Playlist: The found playlist or None if not found.
        """
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist
        return None

    def calculate_average_rating(self):
        """
        Calculates the average rating of all playlists.

        Returns:
        - float: The average rating.
        """
        total_ratings = 0
        total_playlists = len(self.playlists)

        for playlist in self.playlists:
            total_ratings += playlist.get_average_rating()

        return total_ratings / total_playlists

    def customize_player(self, theme):
        """
        Customizes the player with the specified theme.

        Parameters:
        - theme (str): The theme to apply.

        Returns:
        - bool: True if customization is successful, False otherwise.
        """
        return True

