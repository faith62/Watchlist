from distutils.log import debug
from app import app

if __name__ == '_main_': # check if the script is run directly 
    app.run(debug = True) #debug=True allow us us run on debug mode, to easily track errors