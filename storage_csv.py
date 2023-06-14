
from istorage import IStorage
import requests


API_KEY = "cfb1ce63"


class StorageCsv(IStorage):
    """ Inherits from Storage and implements its functions."""

    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
            Returns a dictionary of dictionaries that
            contains the movies information in the database.
        """
        with open("data.json", "r") as fileobj:
            movies_data = fileobj.read()
            movies_saved = json.loads(movies_data)
        return movies_saved

    def add_movie(self, title, year, rating, poster):
        """
            Adds a movie to the movie database.
            Loads the information from the JSON file, add the movie,and saves it.
        """
        API_MOVIE_URL = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
        res = requests.get(API_MOVIE_URL)
        movies_data = json.loads(res.text)
        print(f'Movie {movies_data["Title"]} successfully added')

        with open("data.json", "r") as handle:
            exist_data = json.loads(handle.read())

        new_movie_data = {
            movies_data["Title"]: {
                "year": movies_data["Year"],
                "rating": movies_data["imdbRating"],
                "image": movies_data["Poster"]
            }
        }
        new_dict = {**exist_data, **new_movie_data}

        with open("data.json", "w") as save_file:
            json_file = json.dumps(new_dict)
            saved_movies = save_file.write(json_file)
        return saved_movies

    def delete_movie(self, title):
        """Deletes a movie from the movies database"""
        exist_movies_data = self.list_movies()
        del (exist_movies_data[title])
        with open("data.json", "w") as save_file:
            json.dump(exist_movies_data, save_file)
        return

    def update_movie(self, title, notes):
        """Updates a movie from the movies database"""
        self.new_rating = notes
        movies_data = self.list_movies()
        print(movies_data)
        # movie_update = {}
        for key, val in movies_data.items():
            if title == key:
                val["rating"] = self.new_rating
            movie_update = movies_data.update({key: self.new_rating})
            print(movie_update)
        #     with open("data.json", "w") as save_file:
        #     json.dump(movie_update, save_file)
        # print(movies_data)
