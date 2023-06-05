import requests
import json


API_KEY = "cfb1ce63"


def list_movies():
    """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.
     """
    with open("data.json", "r") as fileobj:
        movies_data = fileobj.read()
        movies_saved = json.loads(movies_data)
    return movies_saved


def add_movies(title):
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


def delete_movies(title):
    """Deletes a movie from the movies database"""
    exist_movies_data = list_movies()
    del(exist_movies_data[title])
    with open("data.json", "w") as save_file:
        json.dump(exist_movies_data, save_file)
    return


def update_movies(title, rating):
    """Updates a movie from the movies database"""
    movies_data = list_movies()
    title = movies_data["Title"]
    rating = movies_data["imdbRating"]
    movies_update = movies_data.update({title: rating})
    with open("data.json", "w") as save_file:
        json.dump(movies_data, save_file)
    return movies_update, rating
