#  create our index page view function
from flask import render_template,request,redirect,url_for
from . import main
from app.requests import get_movie,get_movies,search_movie
from .forms import ReviewForm
from ..models import Review


#views
@main.route('/') #route decorator   localhost:5000/
def index():  #define view function
    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular movie
    popular_movies = get_movies('popular') #from request.py all get movies(category)
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    
    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')#When we submit the form inside our index.html it creates a query with the name of the input movie_query and the value as the input value. We get the query in our view function using request.args.get()function. We pass in the name of the query and the value is returned.

    if search_movie:
        return redirect(url_for('.index',movie_name=search_movie))
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie ) # pass result the variable as an argument 

@main.route('/movie/<int:id>')# localhost:5000/movie/id #route decorator,int to transform content to integer
def movie(id):  #define view function
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)

    return render_template('movie.html',title = title,movie = movie, reviews=reviews)

@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)

