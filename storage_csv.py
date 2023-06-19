from istorage import IStorage
import json
import csv
import requests
import pandas as pd


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
        with open("movies.csv", "r") as csvfile:
            movies_data = csv.DictReader(csvfile)
            current_dict = {}
            for row in movies_data:
                new_dict = {row["title"]: {k: v for k, v in row.items() if k != "title"}}
                current_dict.update(new_dict)
            return current_dict

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

        csv_line = [movies_data["Title"], movies_data["Year"], movies_data["imdbRating"], movies_data["Poster"]]

        with open("movies.csv", "a", newline="") as saved_file:
            writer = csv.writer(saved_file)
            csvwriter = writer.writerow(csv_line)
            return csvwriter

    def delete_movie(self, title):
        """Deletes a movie from the movies database"""
        exist_movies_data = self.list_movies()
        #print(exist_movies_data)

        # df = pd.read_csv('movies.csv')
        # df = df.drop(df[df.title==exist_movies_data[title]].index)
        # df.to_csv('movies.csv', index= False)
        # print(exist_movies_data)

        # with open("movies.csv", "w", newline="") as output:
        #     writer = csv.writer(output)
        #     for key, value in exist_movies_data.items():
        #         if key != title:
        #             writer.writerow(key)
        #             print(f'{key}:{value["rating"]}')

        del exist_movies_data[title]
        print(exist_movies_data)
        for key, value in exist_movies_data.items():
            csv_line = [key, value["year"], value["rating"], value["image"]]

            with open("movies.csv", "a", newline="") as saved_file:
                writer = csv.writer(saved_file)
                csvwriter = writer.writerow(csv_line)
                return csvwriter

    def update_movie(self, title, new_rating):
        """Updates a movie from the movies database with a new rating"""
        movies_data = self.list_movies()
        for key, val in movies_data.items():
            if title == key:
                val["rating"] = new_rating
            with open("movies.csv", "w", newline="") as save_file:
                writer = csv.writer(save_file)
                csvwriter = writer.writerow(movies_data)
                return csvwriter
