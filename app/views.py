#  create our index page view function
from flask import render_template
from app import app

#views
@app.route('/') #route decorator
def index():  #define view function
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')