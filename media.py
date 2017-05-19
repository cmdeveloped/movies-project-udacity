import webbrowser


class Movie():
    '''
        Defining method __init__ to take in movie attributes
        of title, storyline, poster image, and youtube trailer
    '''
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''
            Defining a current instance of class Movie using the __init__ method.
            Referring to an instance calling the method using self.
        '''
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''
            Method show_trailer opens youtube trailer when called.
        '''
    
        webbrowser.open(self.trailer_youtube_url)


