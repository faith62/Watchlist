#write code to make requests to our API.

import urllib.request,json #urllib.request create a connection to our API URL and send a request and json modules that will format the JSON response to a Python dictionary.

# from app.movie_test import Movie
from .models import Movie

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']  #api key=f4c698a6dcd23f4fbaf57758faa0f910
    base_url = app.config['MOVIE_API_BASE_URL']  #https://api.themoviedb.org/3/movie/{}?api_key={}




def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key) #replace the {} curly brace placeholders in the base_url with the category and api_key

    with urllib.request.urlopen(get_movies_url) as url: #with context manager to send request url to hold response back
        get_movies_data = url.read() #from buffer to json ,to be understood by browser, read() read response
        get_movies_response = json.loads(get_movies_data) #fron json to python dictionary

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results#list of movie objects

def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object

def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = [] # store our newly created movie objects.


    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        
        movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
        movie_results.append(movie_object)

    return movie_results#list of movie objects

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results


    
