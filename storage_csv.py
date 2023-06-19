import os.path
from istorage import IStorage
import json
import csv
import requests


API_KEY = "cfb1ce63"


class StorageCsv(IStorage):
    """ Inherits from Storage and implements its functions."""

    def __init__(self, storage_csv):
        self.storage_csv = storage_csv
        self._create_storage_if_not_exist()

    def _create_storage_if_not_exist(self):
        """
            Check is the storage_csv file exist, if it does,
            the function return without doing anything.
            If not, create a new storage CSV file
        """
        if os.path.exists(self.storage_csv):
            return

        with open(self.storage_csv, 'w') as csvfile:
            fieldnames = ['title', 'rating', 'year', 'image']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    def _load_db(self):
        """ Load the data from the database."""
        data = {}
        with open(self.storage_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data[row['title']] = row
        return data

    def _save_db(self, movies):
        """ Save the data to the csv file."""
        with open(self.storage_csv, 'w') as csvfile:
            fieldnames = ['title', 'rating', 'year', 'image']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for movie_data in movies.values():
                writer.writerow(movie_data)

    def list_movies(self):
        """
            Returns a dictionary of dictionaries that
            contains the movies information in the database.
        """
        list_movies = self._load_db()
        return list_movies

    def add_movie(self, title):
        """
            Adds a movie to the movie database.
            Loads the information from the JSON file, add the movie,
            and saves it to CSV file.
        """
        API_MOVIE_URL = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
        res = requests.get(API_MOVIE_URL)
        movies_data = json.loads(res.text)

        print(f'Movie {movies_data["Title"]} successfully added')

        with open("movies.csv", "r") as handle:
            csv.reader(handle)

        csv_line = [movies_data["Title"], movies_data["imdbRating"], movies_data["Year"], movies_data["Poster"]]

        with open("movies.csv", "a", newline="") as saved_file:
            writer = csv.writer(saved_file)
            csvwriter = writer.writerow(csv_line)
            return csvwriter

    def delete_movie(self, title):
        """Deletes a movie from the movies database"""
        exist_movies_data = self._load_db()
        del exist_movies_data[title]
        self._save_db(exist_movies_data)

    def update_movie(self, title, new_rating):
        """Updates a movie from the movies database with a new rating"""
        movies_data = self._load_db()
        for key, val in movies_data.items():
            if title == key:
                val["rating"] = new_rating
                self._save_db(movies_data)

