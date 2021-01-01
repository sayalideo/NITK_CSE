from flask import render_template, flash, redirect, url_for
from nitk_cse.models import User, News
from nitk_cse.forms import LoginForm, NewsForm
from nitk_cse import app, db

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

@app.route('/add_news',methods=['GET','POST'])
def add_news():
    form = NewsForm()
    news = News.query.all()
    if form.validate_on_submit():
        n = News(news=form.news.data,link=form.link.data,link_text=form.link_text.data)
        db.session.add(n)
        db.session.commit()
        flash(f'News Added Successfully!','success')
        return redirect(url_for('add_news'))
    return render_template('add_news.html',form=form,news=news)
