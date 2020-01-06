import fresh_tomatoes
import media

# This section is used to initialize the values in the Movie Class

mechanic = media.Movie("The Mechanic",
                       '''One of an elite group of assassins,
                          Arthur Bishop (Jason Statham)
                          may be the best in the business.''',
                       "https://www.iceposter.com/thumbs/MOV_c276856c_b.jpg",
                       "https://www.youtube.com/watch?v=CMklQNn0OH0")


avatar = media.Movie("Avatar",
                      '''A marine on an alien planet.
                      How the common people will survire
                      in the alien planet?''',
                      "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY") 


resident_evil = media.Movie("Resident Evil: The Final Chapter",
                            '''The T virus unleashed by the evil Umbrella
                            Corp has spread to every corner
                             of the globe, infesting the planet with
                             zombies, demons and monsters.''',
                             "https://i.ebayimg.com/images/i/223423674414-0-1/s-l1000.jpg",  # noqa
                             "https://www.youtube.com/watch?v=79Sd4GtOXuI")


matrix = media.Movie("Matrix",
                     '''A computer hacker learns from mysterious rebels
                     about the true nature of his reality.''',
                     "https://www.movieposter.com/posters/archive/main/9/A70-4902",  # noqa
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")


mad_max_fury_road = media.Movie("Mad Max Fury Road",
                                '''In a stark desert landscape where humanity
                                is broken, two rebels just might
                                be able to restore order.''',
                                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdNjbYvLs3mM8JlN93ahmqJ316RlfzBOTaUr_i6qV0Zys_Iwk1UQ",  # noqa
                                "https://www.youtube.com/watch?v=YWNWi-ZWL3c")


whiplash = media.Movie("Whiplash",
                       '''A promising young drummer enrolls at a
                       cut-throat music conservatory
                       where his dreams of
                       greatness are mentored by an instructor.''',
                       "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSyLORvKKvCi7-vy8vwi2s8F62aG7D36H15A8rOVfP2d7koyA9I",  # noqa
                       "https://www.youtube.com/watch?v=tYkuvB2f5XU")


# "import fresh_tomatoes" allows to turn this code into a movie website
# The "open_movies_page" function takes a list of movies, then opens it
movies = [mechanic, avatar, resident_evil, matrix, mad_max_fury_road, whiplash]
fresh_tomatoes.open_movies_page(movies)