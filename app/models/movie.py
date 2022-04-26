class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id  #the movie id
        #Title - The name of the movie
        self.title = title
        #Overview - A short description on the movie
        self.overview = overview
        #image- The poster image for the movie
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        #vote_average - Average rating of the movie
        self.vote_average = vote_average
        #vote_count - How many people have rated the movie
        self.vote_count = vote_count