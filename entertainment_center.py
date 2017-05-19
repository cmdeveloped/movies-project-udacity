import media
import fresh_tomatoes


# Movie instances that I have selected with attribute of class Movie
moana = media.Movie("Moana",
                    "In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches an impetuous "
                    "Chieftain's daughter's island, she answers the Ocean's call to seek out the Demigod to set things right.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI@._V1_UX182_CR0,0,182,268_AL_.jpg", # noqa
                    "https://www.youtube.com/watch?v=M5dnZKrUpdA")

big_hero = media.Movie("Big Hero 6",
                       "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro "
                       "Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYtMGM0NDc1YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_UY268_CR3,0,182,268_AL_.jpg", # noqa
                       "https://www.youtube.com/watch?v=z3biFxZIJOQ")

frozen = media.Movie("Frozen",
                     "When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home "
                     "in infinite winter, her sister, Anna, teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg", # noqa
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

tangled = media.Movie("Tangled",
                      "The magically long-haired Rapunzel has spent her entire life in a tower, but now that a runaway thief "
                      "has stumbled upon her, she is about to discover the world for the first time, and who she really is.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAxNDYxMjg0MjNeQTJeQWpwZ15BbWU3MDcyNTk2OTM@._V1_UX182_CR0,0,182,268_AL_.jpg", # noqa
                      "https://www.youtube.com/watch?v=2f516ZLyC6U")

inside_out = media.Movie("Inside Out",
                         "After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions "
                         "- Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UX182_CR0,0,182,268_AL_.jpg", # noqa
                         "https://www.youtube.com/watch?v=seMwpP0yeu4")

monsters_uni = media.Movie("Monsters University",
                           "A look at the relationship between Mike and Sulley during their days at Monsters University "
                           "-- when they weren't necessarily the best of friends.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyODgwMDU3M15BMl5BanBnXkFtZTcwOTM4MjcxOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg", # noqa
                           "https://www.youtube.com/watch?v=ODePHkWSg-U")


# Extras
good_dinosaur = media.Movie("The Good Dinosaur",
                            "In a world where dinosaurs and humans live side-by-side, an" 
                            "Apatosaurus named Arlo makes an unlikely human friend.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5MTg2NjQ4MV5BMl5BanBnXkFtZTgwNzcxOTY5NjE@._V1_UX182_CR0,0,182,268_AL_.jpg", # noqa
                            "https://www.youtube.com/watch?v=O-RgquKVTPE")

zootopia = media.Movie("Zootopia",
                       "In a city of anthropomorphic animals, a rookie bunny cop and a cynical con" 
                       "artist fox must work together to uncover a conspiracy.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_UX182_CR0,0,182,268_AL_.jpg", # noqa
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")


# Movie array containing each instance. 
movies = [moana, big_hero, frozen, tangled, inside_out, monsters_uni, good_dinosaur, zootopia]

# Calling method open_movies_page and passing in the array in which to display. 
fresh_tomatoes.open_movies_page(movies)
