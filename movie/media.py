import webbrowser

"""contains movie class for storing movie object attributes."""

class Movie():
    def __init__(self,movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """stores movie attributes.
        Args:
            movie_title: string variable.
            movie_storyline: string variable.
            poster_image: movie poster's link as a string variable.
            trailer_youtube: movie trailer's youtube link as a string
                           variable.
        """
        #Assign movie attributes
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


        
        
