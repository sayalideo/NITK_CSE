from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm, NewsForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = '9cda09e832928e461cdd567c2e2249c4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news = db.Column(db.String(120), unique=True, nullable=False)
    link = db.Column(db.String(120), unique=True, nullable=False)
    link_text = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"News('{self.news}')"

@app.route("/")
def hello():
    return 'hi'
    #return render_template('home.html')

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@nitk.edu.in' and form.password.data == 'admin':
            flash(f'Login Succesful!','success')
            return redirect(url_for('admin'))
        else:
            flash(f'Login Unsuccesful!','danger')
    return render_template('login.html',form=form)

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route('/add_news')
def add_news():
    return 'hi'

if __name__ == '__main__':
    app.run(debug=True)