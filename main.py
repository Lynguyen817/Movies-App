from movie_app import MovieApp
from storage_json import StorageJson
import movie_storage
import random


def main():
    storage = StorageJson('movies.json')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()




# def command_add_movie():
#     """Adds a movie to the movies database"""
#     # Get the data from the JSON file
#     movies = movie_storage.list_movies()
#
#     title = input("Enter new movie name:")
#     if title in movies:
#         print(f"Movie {title} already exist!")
#         return
#
#     # Add the movie and save the data to the JSON file
#     movie_storage.add_movies(title)


# def command_delete_movie():
#     """Deletes a movie from the movies database"""
#     # Get the data from the JSON file
#     movies = movie_storage.list_movies()
#     # Delete the movie
#     movie_delete = input("Enter movies name to delete:")
#     if movie_delete not in movies:
#         print("This movie doesn't exist.")
#     else:
#         movie_storage.delete_movies(movie_delete)
#         print(f"Movie {movie_delete} successfully deleted")
#
#
# def command_update_movie(title):
#     """Updates a movie from the movies database"""
#     # Get the data from the JSON file
#     movies = movie_storage.list_movies()
#     # Update the move
#     movie_update = input("Enter movies name:")
#     if movie_update not in movies:
#         print("This movie doesn't exist.")
#     else:
#         new_rating = input("Enter new movie rating(0-10):")
#         movie_storage.update_movies(title, new_rating)
#         print(f"Movie {movie_update} successfully updated")
#


