from flask import render_template, flash, redirect, url_for
from nitk_cse.models import User, News, Research, ResearchJournal, ResearchConf, ResearchFaculty, Professor
from nitk_cse.forms import LoginForm, NewsForm, ResearchAreaForm, JournalForm, ConferenceForm, FacultyForm, ProfessorForm
from nitk_cse import app, db

import os
import secrets
from PIL import Image
from flask import current_app

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

@app.route('/add_research_area',methods=['GET','POST'])
def add_research_area():
    form = ResearchAreaForm()
    areas = Research.query.all()
    if form.validate_on_submit():
        r = Research(title = form.title.data)
        db.session.add(r)
        db.session.commit()
        flash(f'Research Area Added Successfully!','success')
        return redirect(url_for('add_research_area'))
    return render_template('add_research_area.html',form=form,areas=areas)

@app.route('/edit_area/<id>',methods=['GET','POST'])
def edit_area(id):
    j = ResearchJournal.query.filter_by(area_id=id)
    c = ResearchConf.query.filter_by(area_id=id)
    f = ResearchFaculty.query.filter_by(area_id=id)
    return render_template('edit_area.html',j=j,c=c,f=f,id=id)

@app.route('/add_journal/<id>',methods=['GET','POST'])
def add_journal(id):
    jf = JournalForm()
    ra = Research.query.get(id)
    j = ResearchJournal.query.filter_by(area_id=id)
    if jf.submit.data and jf.validate_on_submit():
        r = ResearchJournal(name = jf.name.data, research_area = ra)
        db.session.add(r)
        db.session.commit()
        flash(f'Research Journal Added Successfully!','success')
        return redirect(url_for('edit_area',id=id))
    return render_template('addJournal.html',jf=jf,j=j)

@app.route('/add_conf/<id>',methods=['GET','POST'])
def add_conf(id):
    cf = ConferenceForm()
    ra = Research.query.get(id)
    c = ResearchConf.query.filter_by(area_id=id)
    if cf.submit.data and cf.validate_on_submit():
        r = ResearchConf(name = cf.name.data, research_area = ra)
        db.session.add(r)
        db.session.commit()
        flash(f'Research Conference Added Successfully!','success')
        return redirect(url_for('edit_area',id=id))
    return render_template('addConf.html',cf=cf,c=c)

@app.route('/add_faculty/<id>',methods=['GET','POST'])
def add_faculty(id):
    ff = FacultyForm()
    ra = Research.query.get(id)
    f = ResearchFaculty.query.filter_by(area_id=id)
    if ff.submit.data and ff.validate_on_submit():
        r = ResearchFaculty(name = ff.name.data, research_area = ra)
        db.session.add(r)
        db.session.commit()
        flash(f'Research Faculty Added Successfully!','success')
        return redirect(url_for('edit_area',id=id))
    return render_template('addFaculty.html',ff=ff,f=f)

def save_img(form_picture):
    random_hex   = secrets.token_hex(8)
    _, f_ext     = os.path.splitext(form_picture.filename)
    picture_fn   = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/prof_img', picture_fn)
    output_size  = (256,256)
    i            = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/add_professors',methods=['GET','POST'])
def add_professors():
    form = ProfessorForm()
    hod = Professor.query.filter_by(title='Head of Department')
    prof = Professor.query.filter_by(title='Professor')
    assi = Professor.query.filter_by(title='Assistant Professor')
    asso = Professor.query.filter_by(title='Associate Professor')
    if form.validate_on_submit():
        print('here ',form.picture.data)
        if form.picture.data :
            print('here ',form.picture.data)
            picture_file = save_img(form.picture.data)
        else:
            picture_file = 'icon.png'
        print('pic file ',picture_file)
        prof = Professor(name=form.name.data, title=form.post.data, image_file=picture_file)
        db.session.add(prof)
        db.session.commit()
        return redirect(url_for('add_professors'))
    return render_template('addProfessors.html',form=form, hod=hod, prof=prof, assi=assi, asso=asso)
