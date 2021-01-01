from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm, NewsForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9cda09e832928e461cdd567c2e2249c4'
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