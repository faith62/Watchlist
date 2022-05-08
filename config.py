from instance.config import MOVIE_API_KEY
import os


class Config:  
    '''
    General configuration parent class
    contains configurations that are used in both production and development stages
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}' # {} to represent sections in the URL that will be replaced with actual values
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')





class ProdConfig(Config):
    '''
    Production  configuration child class

    Contains configurations that are used in production stages of our application and inherits from the parent 

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Contains configurations that are used in development stages of our application and inherits from the parent

    Args:
        Config: The parent configuration class with General configuration settings
    '''

DEBUG = True

config_options = {         #create a dictionary config_options to help us access different configuration option classes.
'development':DevConfig,
'production':ProdConfig
}