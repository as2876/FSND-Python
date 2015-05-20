import webbrowser

"""This class provides a way to store movie related information."""

class Movie(object):

    VALID_RATINGS = ("G", "PG", "PG-13", "R")

    def __init__(self,
                 movie_title,
                 poster_image,
                 trailer_youtube,
                 year_made,
                 runtime,
                 rating,
                 mythoughts
                 ):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year_made = year_made
        self.runtime =("{:0>2d}".format(runtime/60)
           +":"+"{:0>2d}".format(runtime - runtime/60*60))
        self.rating = rating
        self.mythoughts = mythoughts

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
