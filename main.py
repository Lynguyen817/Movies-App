import movie_storage
import random


def movies_database(movie):
    """
        Show all the options to the user. Return the result of each user's choice.
        Return the list of the options after the user choose 1 option and press enter.
    """
    for choice in range(0, 100):
        print("""
        Menu:
        0.Exit
        1.List movies
        2.Add movies
        3.Delete movie
        4.Update movie
        5.Stats
        6.Random movie
        7.Search movie
        8.Movies sorted by rating
        9. Generate Website
        """)
        user_choice = int(input("Enter choice(1-8):"))
        if user_choice == 0:
            exit_command()
        if user_choice == 1:
            list_movies()
        if user_choice == 2:
            add_movies()
        if user_choice == 3:
            delete_movies()
        if user_choice == 4:
            update_movies(movie)
        if user_choice == 5:
            statistics(movie)
        if user_choice == 6:
            random_movies(movie)
        if user_choice == 7:
            search_movies(movie)
        if user_choice == 8:
            movies_sorted_by_rating(movie)
        if user_choice == 9:
            generate_website()
        input("Press enter to continue")


def main():
    """ Run the movie_database associate with movie_storage. """
    print("********** My Movies Database **********")
    movies_database(movie_storage)


def exit_command():
    """When the user enters 0, print Bye! then exit """
    for i in range(10):
        if i == 0:
            print("Bye!")
            exit()


def list_movies():
    """List all the movies in the database"""
    # Get the data from the JSON file
    movies = movie_storage.list_movies()
    # Count the number of movies and list them
    total = 0
    for key, value in movies.items():
        total += 1
        print(f'{key}: {value["rating"]}')
    print(f'{total} movies in total.')


def add_movies():
    """Adds a movie to the movies database"""
    # Get the data from the JSON file
    movies = movie_storage.list_movies()

    title = input("Enter new movie name:")
    if title in movies:
        print(f"Movie {title} already exist!")
        return

    # Add the movie and save the data to the JSON file
    movie_storage.add_movies(title)


def delete_movies():
    """Deletes a movie from the movies database"""
    # Get the data from the JSON file
    movies = movie_storage.list_movies()
    # Delete the movie
    movie_delete = input("Enter movies name to delete:")
    if movie_delete not in movies:
        print("This movie doesn't exist.")
    else:
        movie_storage.delete_movies(movie_delete)
        print(f"Movie {movie_delete} successfully deleted")


def update_movies(title):
    """Updates a movie from the movies database"""
    # Get the data from the JSON file
    movies = movie_storage.list_movies()
    # Update the move
    movie_update = input("Enter movies name:")
    if movie_update not in movies:
        print("This movie doesn't exist.")
    else:
        new_rating = input("Enter new movie rating(0-10):")
        movie_storage.update_movies(title, new_rating)
        print(f"Movie {movie_update} successfully updated")


def statistics(movies):
    """
        Return the average rating of all movies in the list.
        Return the median rate.
        Return the best movie with its rating.
        Return the worst movie with its rating.
    """
    # Average rating in the database
    movies = movie_storage.list_movies()
    sum_of_rating = 0
    total_movies = 0
    for key, value in movies.items():
        rating = value["rating"]
        if rating == "N/A":
            pass
        else:
            sum_of_rating += float(rating)
            total_movies += 1
            average = round(float(sum_of_rating / total_movies), 2)
    print(f"Average rating: {average}")

    # Median rating
    for rate in movies.values():
        rating_sorted_list = sorted(rate["rating"])
        n = len(rating_sorted_list)
        if n % 2 == 0:
            median = (rating_sorted_list[n // 2 - 1] + rating_sorted_list[n // 2]) / 2
        else:
            median = rating_sorted_list[n // 2]
    print(f"Median rating: {median}")

    # The best movie
    list_of_best_movie = {}
    max_rate = 0
    for name, rate in movies.items():
        if rate["rating"] == "N/A":
            pass
        else:
            if float(rate["rating"]) > max_rate:
                max_rate = float(rate["rating"])
                list_of_best_movie[name] = max_rate
    print(f"Best Movie: {name}, {max_rate}")

    # The worst movie
    list_of_worst_movie = {}
    for name, rate in movies.items():
        if rate["rating"] == "N/A":
            pass
        else:
            min_rate = float(rate["rating"])
            if float(rate["rating"]) < min_rate:
                min_rate = float(rate["rating"])
                list_of_worst_movie[name] = min_rate
    print(f"Worst movie: {name}, {min_rate}")


def random_movies(movies):
    """ Get a random movie from the list of movies. """
    # Get the data from the JSON file
    movies = movie_storage.list_movies()

    for item in movies.items():
        random.choice(item)
    print(f"Your movie for tonight: {item[0]}, it's rated {item[1]['rating']}")


def search_movies(movies):
    """ Search a movie by name."""
    movie_search = input("Enter part of movie name: ")
    # Get the data from the JSON file
    movies = movie_storage.list_movies()

    search_movies_list = {}
    for name, rate in movies.items():
        if movie_search in name:
            if name not in search_movies_list:
                search_movies_list[name] = rate
            print(f"{name}, Year: {rate['year']}, Rating: {rate['rating']}")
    print(f"Movie {movie_search} is not in the list.")


def movies_sorted_by_rating(movies):
    """
        Get the data from JSON file
        then sort them by rating from highest to lowest.
    """
    movies = movie_storage.list_movies()

    new_list = []
    for name, rating in movies.items():
        movies[name] = rating
        rate = rating["rating"]
        new_list.append([name, rate])
    new_sorted_list = sorted(new_list, key=lambda x: x[1], reverse=True)
    for i in new_sorted_list:
        print(f'{i[0]}: {i[1]}')


def serialize_movie(movie_obj):
    """
        Get the image of movies from the JSON file
        then serialize them
    """
    movies = movie_storage.list_movies()
    output = ""
    output += '<li>'
    output += f'<div class="container">'
    for key, value in movies.items():
        image_link = value["image"]
        year = value["year"]
        rating = value["rating"]
        output += f'<div class="movie">'
        output += f'<img class="movie-poster" src="{image_link}">'
        output += f'<div class="movie-title">{key}</div>'
        output += f'<div class="movie-year">{year}</div>'
        output += f'<div class="movie-rate">{rating}</div>'
        output += f'</div>'
    output += f'</div>'
    output += '</li>'
    return output


def generate_website():
    """
        Generate the website.
        Read the index_template file then write a new html file
    """
    with open("_static/index_template.html", "r") as fileobj:
        movies_info = fileobj.readlines()

    for movie_obj in movie_storage.list_movies():
        output = serialize_movie(movie_obj)

    line_replace = "__TEMPLATE_MOVIE_GRID__"
    with open("_static/index.html", "w") as newfile:
        for line in movies_info:
            newfile.write(line.replace(line_replace, output))
        print("Website was generated successfully.")


if __name__ == "__main__":
    main()


