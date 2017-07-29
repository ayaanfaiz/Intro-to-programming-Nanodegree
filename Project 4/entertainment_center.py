#imports files named fresh_tomatoes and media
import fresh_tomatoes
import media
#The detail of movie used in the web page
the_boss_baby = media.Movie("The Boss Baby",
                        "A new baby's arrival impacts a family, told from the point of view of a delightfully unreliable narrator -- a wildly imaginative 7-year-old named Tim.",
                        "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
                        "https://www.youtube.com/watch?v=O2Bsw3lrhvs")
dunkirk = media.Movie("Dunkirk",
                     "In May 1940, Germany advanced into France, trapping Allied troops on the beaches of Dunkirk. Under air and ground cover from British and French forces, troops were slowly and methodically evacuated from the beach using every serviceable naval and civilian vessel that could be found.",
                     "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                     "https://www.youtube.com/watch?v=T7O7BtBnsG4")
passengers = media.Movie("Passengers",
                         "On a routine journey through space to a new home, two passengers, sleeping in suspended animation, are awakened 90 years too early when their ship malfunctions.",
                         "https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")
la_la_land = media.Movie("La La Land",
                         "Sebastian (Ryan Gosling) and Mia (Emma Stone) are drawn together by their common desire to do what they love.",
                         "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                         "https://www.youtube.com/watch?v=0pdqf4P9MB8")
beauty_and_the_beast = media.Movie("Beauty and the Beast",
                                   "Belle (Emma Watson), a bright, beautiful and independent young woman, is taken prisoner by a beast (Dan Stevens) in its castle.",
                                   "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                                   "https://www.youtube.com/watch?v=e3Nl_TCQXuw")
despicable_me_3 = media.Movie("Despicable Me 3",
                              "The mischievous Minions hope that Gru will return to a life of crime after the new boss of the Anti-Villain League fires him. Instead, Gru decides to remain retired and travel to Freedonia to meet his long-lost twin brother for the first time.",
                              "https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg",
                              "https://www.youtube.com/watch?v=Rlq39IC07qA")
#Saves the variable name and then calls the opens_movie_page function in the fresh_tomatoes file
movies = [the_boss_baby, dunkirk, passengers, la_la_land, beauty_and_the_beast, despicable_me_3]
fresh_tomatoes.open_movies_page(movies)
