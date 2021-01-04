from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, SubmitField, StringField, PasswordField, RadioField, IntegerField
from flask_wtf.file import FileField, FileAllowed, FileRequired
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

class ProfessorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=200)])
    post = RadioField('Post', validators=[DataRequired()], choices=[('Professor','Professor'),('Head of Department','Head of Department'),('Associate Professor','Associate Professor'),('Assistant Professor','Assistant Professor')])
    picture = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'], FileRequired())])
    submit = SubmitField('Add Faculty')

class CSFYForm(FlaskForm):
    picture = FileField('Upload File', validators=[FileAllowed(['jpg', 'png', 'jpeg'], FileRequired())])
    submit = SubmitField('Add List')

class ISFYForm(FlaskForm):
    picture = FileField('Upload File', validators=[FileAllowed(['jpg', 'png', 'jpeg'], FileRequired())])
    submit = SubmitField('Add List')

class CSSYForm(FlaskForm):
    picture = FileField('Upload File', validators=[FileAllowed(['jpg', 'png', 'jpeg'], FileRequired())])
    submit = SubmitField('Add List')

class ISSYForm(FlaskForm):
    picture = FileField('Upload File', validators=[FileAllowed(['jpg', 'png', 'jpeg'], FileRequired())])
    submit = SubmitField('Add List')

class RDForm(FlaskForm):
    name = TextAreaField('Enter Project Details', validators=[DataRequired(), Length(min=2, max=200)])
    submit = SubmitField('Add Project')

class ConsultancyForm(FlaskForm):
    title = TextField('Add Title of Consultancy', validators=[Length(max=100)])
    guide = TextField('Add Name of the Guide/ Investigator', validators=[Length(max=100)])
    agency = TextField('Add Funding Agency ', validators=[Length(max=100)])
    student = TextField('Add Name of the Student Involved', validators=[Length(max=100)])
    status = TextField('Status/ Amt.', validators=[Length(max=100)])
    year = IntegerField('Year')
    submit = SubmitField('Add Consultancy')
