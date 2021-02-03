from Song import Song


class Playlist:
    def __init__(self):
        self.__first_song = None

    # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

    def add_song(self, title):
        new_song = Song(title)

        if (self.__first_song == None):
            self.__first_song = new_song
            return

        # else traverse till last song
        last_song = self.__first_song
        while(last_song.__next_song):
            last_song = last_song.next

        # Change the next of the last song
        last_song.next = new_song

    # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

    def find_song(self, title):
        pass
        # index = 0
        # while index < len(Playlist):
        #     if title == Playlist[index]:
        #         return index
        #     else:
        #         index += 1

        # return None

    # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed.

    def remove_song(self, title):
        # store first song
        curr = self.__first_song
        # if the first song is to be deleted
        if(curr is not None):
            if(curr.__title == title):
                self.__first_song = curr.__next_song
                curr = None
                return
        # keep searching using next song
        while(curr is not None):
            if (curr.__title == title):
                break
            prev = curr
            curr = curr.__next_song

        # Unlink the node from Playlist
        prev.next = curr.__next_song
        curr = None

    # TODO: Create a method called length, which returns the number of songs in the playlist.

    def length(self):
        return len(Playlist)

    # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

    # Example:
    # 1. Song Title 1
    # 2. Song Title 2
    # 3. Song Title 3

    def print_songs(self):

        current_song = self.__first_song
        counter = 0
        while current_song != None:
            print(current_song.__title)
            print(f"{counter + 1}. {current_song.get_title()}")
            counter += 1
            current_song = current_song.get_next_song()
