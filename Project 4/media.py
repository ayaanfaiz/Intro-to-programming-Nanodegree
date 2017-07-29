#imports clases included in the webbrowser library to open webpage in the browser
import webbrowser
#Defines class movie to save all the details included in the web page.
class Movie():
    #__init__ function gets called automatically to initialise values to local variable
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Open the webpage
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
