from Song import Song


class Playlist:
    def __init__(self):
        self.__first_song = None

    def add_song(self, title):
        new_song = Song(title)
        new_song.set_next_song(self.__first_song)
        self.__first_song = new_song

    def find_song(self, title):
        node = self.__first_song
        counter = 0
        while node != None:
            if node.get_title() == title:
                return counter
            else:
                counter += 1
                node = node.get_next_song()
        return -1

    def remove_song(self, title):
        node = self.__first_song
        temp_node = None

        if self.__first_song.get_title() == title:
            self.__first_song = self.__first_song.get_next_song()
            return

        while node != None:
            temp_node = node
            node = node.get_next_song()
            if node.get_title() == title:
                temp_node.set_next_song(node.get_next_song())
                return True
        return False

    def length(self):
        current_node = self.__first_song
        counter = 0
        while current_node != None:
            counter += 1
            current_node = current_node.get_next_song()
        return counter

    def print_songs(self):
        node = self.__first_song
        counter = 0
        while node != None:
            print(f"{counter + 1}. {node.get_title()}")
            counter += 1
            node = node.get_next_song()
