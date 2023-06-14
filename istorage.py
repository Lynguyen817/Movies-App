from abc import ABC, abstractmethod


class IStorage(ABC):
    """ Create an interface - abstract class."""
    @abstractmethod
    def list_movies(self):
        pass

    @abstractmethod
    def add_movie(self, title):
        pass

    @abstractmethod
    def delete_movie(self, title):
        pass

    @abstractmethod
    def update_movie(self, title, notes):
        pass
