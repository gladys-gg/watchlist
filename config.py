import os

class Config:
    '''
    General configuration parent class
    '''
    
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key=b971983a88ad8386e3a5fc45ad216960'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Gmwangi@localhost/watchlist'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}