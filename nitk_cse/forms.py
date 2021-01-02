from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class NewsForm(FlaskForm):
    news = TextAreaField('Enter News', validators=[DataRequired(), Length(min=2, max=100)])
    link = TextField('Add a link', validators=[Length(max=100)])
    link_text = TextField('Add text to display above the link', validators=[Length(max=100)])
    submit = SubmitField('Add News')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ResearchAreaForm(FlaskForm):
    title = StringField('Subject', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Add Research Area')

class JournalForm(FlaskForm):
    name = TextAreaField('Enter Details', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Add Journal')

class ConferenceForm(FlaskForm):
    name = TextAreaField('Enter Details', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Add Conference')

class FacultyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Add Faculty')