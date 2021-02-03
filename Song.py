class Song:

    def __init__(self, title, next=None):
        self.__title = title
        self.__next_song = next

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_next_song(self):
        return self.__next_song

    def set_next_song(self, next_title):
        self.__next_song = next_title

    def __str__(self):
        return f'{self.__title}'

    def __repr__(self):
        return '{} -> {}'.format(self.__title, self.__next_song)
