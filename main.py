from movie_app import MovieApp
from storage_json import StorageJson
#from storage_csv import StorageCsv

def main():
    #storage = StorageCsv('movies.csv')
    storage = StorageJson('movies.json')
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()

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


