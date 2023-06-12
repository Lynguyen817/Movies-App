import random
from storage_json import StorageJson


class MovieApp:
    """ Contains all the logic of the movie app(menu, commands etc.)."""
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """List all the movies in the database"""
        movies = self._storage.list_movies()
        # Count the number of movies and list them
        total = 0
        for key, value in movies.items():
            total += 1
            print(f'{key}: {value["rating"]}')
        print(f'{total} movies in total.')

    def _command_movie_statistics(self):
        """
                Return the average rating of all movies in the list.
                Return the median rate.
                Return the best movie with its rating.
                Return the worst movie with its rating.
            """
        # Average rating in the database
        movies = self._storage.list_movies()
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
        for k, v in list_of_best_movie.items():
            if v == max_rate:
                print(f"Best Movie: {k}, {v}")

        # The worst movie
        list_of_worst_movie = {}
        for key, value in movies.items():
            if value["rating"] == "N/A":
                pass
            else:
                min_rate = float(value["rating"])
                list_of_worst_movie[key] = min_rate
        for name, rating in list_of_worst_movie.items():
            if rating < min_rate:
                min_rate = rating
                print(f"Worst movie: {name}, {min_rate}")


    def _command_random_movie(self):
        """ Get a random movie from the list of movies. """
        # Get the data from the JSON file
        movies = self._storage.list_movies()

        lst_movies = []
        for item in movies.items():
            lst_movies.append(item)
        random_movie = random.choice(lst_movies)
        print(f"Your movie for tonight: {random_movie[0]}, it's rated {random_movie[1]['rating']}")

    def _command_search_movie(self):
        """ Search a movie by name."""
        movie_search = input("Enter part of movie name: ")
        movies = self._storage.list_movies()

        search_movies_list = {}
        for name, rate in movies.items():
            if movie_search in name:
                if name not in search_movies_list:
                    search_movies_list[name] = rate
                print(f"{name}, Year: {rate['year']}, Rating: {rate['rating']}")

    def _command_movies_sorted_by_rating(self):
        """
            Get the data from JSON file
            then sort them by rating from highest to lowest.
        """
        movies = self._storage.list_movies()

        new_list = []
        for name, rating in movies.items():
            movies[name] = rating
            rate = rating["rating"]
            new_list.append([name, rate])
        new_sorted_list = sorted(new_list, key=lambda x: x[1], reverse=True)
        for i in new_sorted_list:
            print(f'{i[0]}: {i[1]}')

    def _serialize_movie(self):
        """
            Get the image of movies from the JSON file
            then serialize them
        """
        movies = self._storage.list_movies()
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

    def _generate_website(self):
        """
            Generate the website.
            Read the index_template file then write a new html file
        """
        with open("_static/index_template.html", "r") as fileobj:
            movies_info = fileobj.readlines()

        for movie_obj in self._storage.list_movies():
            output = self._serialize_movie()

        line_replace = "__TEMPLATE_MOVIE_GRID__"
        with open("_static/index.html", "w") as newfile:
            for line in movies_info:
                newfile.write(line.replace(line_replace, output))
            print("Website was generated successfully.")

    def run(self):
        """
            Show all the options to the user. Return the result of each user's choice.
            Return the list of the options after the user choose 1 option and press enter.
        """
        print("********** My Movies Database **********")
        for choice in range(0, 100):
            # Print menu
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
            # When the user enters 0, print Bye! then exit
            if user_choice == 0:
                print("Bye!")
                exit()
            # Get use command and Execute command
            if user_choice == 1:
                self._command_list_movies()
            if user_choice == 2:
                StorageJson.add_movie()
            if user_choice == 3:
                StorageJson.delete_movie()
            if user_choice == 4:
                StorageJson.update_movie()
            if user_choice == 5:
                self._command_movie_statistics()
            if user_choice == 6:
                self._command_random_movie()
            if user_choice == 7:
                self._command_search_movie()
            if user_choice == 8:
                self._command_movies_sorted_by_rating()
            if user_choice == 9:
                self._generate_website()
            input("Press enter to continue")

