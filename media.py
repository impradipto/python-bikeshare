import webbrowser
'''Class movie which contains attributes of movies
   Contains functions show_trailer() which shows trailer.
   Contains init function which initializes the instance variables.'''


class Movie():
    # Initializing and creating space in memory for what we are about to create
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        '''Intializes the variables for the instances.'''            
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        '''Function to open trailer of the instance in the browser'''
        webbrowser.open(self.trailer_youtube_url)