from nitk_cse import db

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
