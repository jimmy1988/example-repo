#START OF ALBUM CLASS
class Album:
    _album_name = "" # The album artist
    _number_of_songs = 0 # The number of songs
    _album_artist = ""

    def __init__(self, album_name = "", number_of_songs = 0, album_artist = "") -> None:

        """
            Initialize an Album object
        Args:
            album_name:
            number_of_songs:
            album_artist:
        """
        self.set_album_name(album_name)
        self.set_number_of_songs(number_of_songs)
        self.set_album_artist(album_artist)

    def set_album_name(self, album_name = "") -> Album:

        """
        Set the album name
        Args:
            album_name (str): The name of the album. Defaults to "".:

        Returns:
            Album: The album object

        """

        self._album_name = str(album_name)
        return self

    def get_album_name(self) -> str:

        """
        Get the album name
        Returns:
            str: The album name

        """

        return self._album_name

    def set_number_of_songs(self, number_of_songs = 0) -> Album:

        """
        Set the number of songs
        Args:
            number_of_songs (int): The number of songs. Defaults to 0.:

        Returns:
            Album: The album object

        """

        self._number_of_songs = int(number_of_songs)
        return self

    def add_songs(self, number_of_songs = 1) -> Album:

        """
        Add songs
        Args:
            number_of_songs (int): The number of songs. Defaults to 0.:

        Returns:
            Album: The album object
        """

        add_songs = self.get_number_of_songs() + number_of_songs
        self.set_number_of_songs(add_songs)
        return self

    def remove_songs(self, number_of_songs = 1) -> Album:

        """
        Remove songs
        Args:
            number_of_songs (int): The number of songs. Defaults to 0.:

        Returns:
            Album: The album object

        """

        remove_songs = self.get_number_of_songs() - number_of_songs
        self.set_number_of_songs(remove_songs)
        return self

    def get_number_of_songs(self) -> int:

        """
        Get the number of songs
        Returns:
            int: The number of songs

        """

        return self._number_of_songs

    def set_album_artist(self, album_artist = "") -> Album:

        """
        Set the album artist
        Args:
            album_artist (str): The album artist. Defaults to "".:

        Returns:
            Album: The album object

        """

        self._album_artist = str(album_artist)
        return self

    def get_album_artist(self) -> str:

        """
        Get the album artist

        Returns:
            str: The album artist

        """

        return self._album_artist

    def __str__(self):
        return f"{self.get_album_name()}, {self.get_album_artist()}, {self.get_number_of_songs()}"

#END OF ALBUM CLASS

#START OF THE MAIN PROGRAM

albums1 = [
    Album(album_name = "25", number_of_songs = 25, album_artist = "Simply Red"),
    Album(album_name = "Greatest Hits", number_of_songs = 34, album_artist = "Rammstein"),
    Album(album_name="Gold", number_of_songs = 59, album_artist = "ABBA"),
    Album(album_name="Celebration", number_of_songs = 36, album_artist = "Madonna"),
    Album(album_name="Essentials", number_of_songs = 24, album_artist = "Metallica"),
]

albums1.sort(key = lambda this_album: this_album.get_number_of_songs())
for album in albums1:
    print(album)

print()

albums1[0], albums1[1] = albums1[1], albums1[0]
for album in albums1:
    print(album)


albums2 = [
    Album(album_name = "Bad", number_of_songs = 40 , album_artist = "Michael Jackson"),
    Album(album_name = "Platinum Collection", number_of_songs = 54, album_artist = "Queen"),
    Album(album_name = "Ta-Dah!", number_of_songs = 13, album_artist = "Scissor Sisters"),
    Album(album_name = "Greatest Hits", number_of_songs = 43, album_artist = "Sophie Ellis-Bextor"),
    Album(album_name = "Human League: Greatest Hist", number_of_songs = 16, album_artist = "Human League"),
]

albums2.extend(albums1)
albums2.append(Album(album_name= "Dark Side of the Moon", number_of_songs = 9, album_artist = "Pink Floyd"))
albums2.append(Album(album_name= "Oops!... I Did It Again", number_of_songs = 16, album_artist = "Britney Spears"))

albums2.sort(key = lambda this_album: this_album.get_album_name())

for album in albums2:
    print(album)

print()

for album in albums2:
    if album.get_album_name() == "Dark Side of the Moon":
        print(albums2.index(album))


#END OF THE MAIN PROGRAM