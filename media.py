import webbrowser

class Movie(object):
    """ This class provides a way to store movie related information.
    
    Attributes:
        title: title of the movie
        storyline: storyline of the movie
        poster_image_url: url of the movie poster image (from wikipedia)
        trailer_youtube_url: url of the youtube trailer    
    """
    
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        """Inits Movie class with the following attributes"""
        self.title=title
        self.storyline=storyline
        self.poster_image_url=poster_image_url
        self.trailer_youtube_url=trailer_youtube_url
        
    def show_trailer(self):
        """Open a broswer window with trailer_youtube_url as the destination"""
        webbrowser.open(self.trailer_youtube_url)
