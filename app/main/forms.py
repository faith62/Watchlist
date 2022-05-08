from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField #help us create a text field, a text Area field and a submit button.
from wtforms.validators import InputRequired # prevent the user from submitting the form without Inputting a value

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Movie review', validators=[InputRequired()])
    submit = SubmitField('Submit')