from media import Movie
import fresh_tomatoes

""" 
This is a list of the data that will be input below.
movie_title
poster_image
trailer_youtube
year_made
runtime
rating
my_thoughts

"""
the_big_chill = Movie("The Big Chill",
                     "http://upload.wikimedia.org/wikipedia/en/5/58/Big_chill_ver1.jpg",
                     "https://www.youtube.com/watch?v=O19k-YtwXTg",
                     "1980",
                     110,
                     "PG-13",
                     "Talk about a great soundtrack!")

pay_it_forward = Movie("Pay it Forward",
                       "https://upload.wikimedia.org/wikipedia/en/d/da/Pay_it_forward_ver1.jpg",
                       "https://www.youtube.com/watch?v=qfW0wCV9iFI",
                       "2000",
                       122,
                       "PG-13",
                       "How can you make a difference?")
                       
                    
marvels_the_avengers = Movie("Marvel's The Avengers",
                             "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                             "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                             "2012",
                             143,
                             "PG",
                             "Gotta love Robert Downey, Jr.!")

no_way_out = Movie("No Way Out",
                   "http://upload.wikimedia.org/wikipedia/en/5/51/No_Way_Out_%281987_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=lypNWLvpb0I",
                   "1987", 
                   114,
                   "R",
                   "A great suspenseful thriller!")
                   
hoosiers = Movie("Hoosiers",
                 "https://upload.wikimedia.org/wikipedia/en/8/8d/Hoosiers_movie_poster_copyright_fairuse.jpg",
                 "https://www.youtube.com/watch?v=xB1M9iv3LOE",
                 "1986",
                 114,
                 "PG-13",
                 "Indiana basketball championship!")

bourne_identity = Movie("Bourne Identity",
                        "http://www.gstatic.com/tv/thumb/movieposters/28900/p28900_p_v7_aa.jpg",
                        "https://www.youtube.com/watch?v=AfkNq0CDx6w",
                        "2002",
                        119,
                        "PG-13",
                        "Am I really who they say I am?")

bourne_supremacy = Movie("Bourne Supremacy",
                         "http://vignette2.wikia.nocookie.net/bourne/images/c/c6/The-bourne-supremacy.jpg/revision/latest?cb=20121106203827",
                         "https://www.youtube.com/watch?v=rmOxVvT5lmw",
                         "2004",
                         108,
                         "PG-13",
                         "Framed for something he didn't do!")

bourne_ultimatum = Movie("Bourne Ultimatum",
                         "https://upload.wikimedia.org/wikipedia/en/f/fe/The_Bourne_Ultimatum_%282007_film_poster%29.jpg",
                         "https://www.youtube.com/watch?v=N6J2oiKJr-A",
                         "2007",
                         115,
                         "PG-13",
                         "Jason Bourne is seeking revenge!")
                         
die_hard = Movie("Die Hard",
                 "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
                 "https://www.youtube.com/watch?v=-qxBXm7ZUTM",
                 "1988",
                 132,
                 "R",
                 "More action from Bruce!")
                 
movies = [the_big_chill, pay_it_forward, marvels_the_avengers, no_way_out, hoosiers, 
          bourne_identity, bourne_supremacy, bourne_ultimatum, die_hard]

fresh_tomatoes.open_movies_page(movies)
 
