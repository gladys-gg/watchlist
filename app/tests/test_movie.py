import unittest
from app.models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    """
    test class to test the behavior of the movie class
    """

    def setUp(self):
        """
        Set up method that will run before every Test  
        """
        self.new_movie = Movie(1234, 'Python Must Be Crazy', 'A thrilling new Python Series', 'https://image.tmbd.org/t/p/w500/khsjha27hbs', 8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,  Movie))


