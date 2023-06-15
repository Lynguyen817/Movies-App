from istorage import IStorage
import csv


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
        dictionary = {}
        with open("movies.csv", "r") as csvfile:
            movies_data = csv.reader(csvfile)
            #movies_dict = {rows[0]:rows[1] for row in movies_data }
            #movies_saved = json.loads(movies_data)
        return movies_data

    def add_movie(self, title):
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

    def update_movie(self, title, new_rating):
        """Updates a movie from the movies database with a new rating"""
        movies_data = self.list_movies()
        for key, val in movies_data.items():
            if title == key:
                val["rating"] = new_rating
                with open("data.json", "w") as save_file:
                    json.dump(movies_data, save_file)
                    return movies_data
