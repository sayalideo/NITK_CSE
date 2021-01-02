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

class Research(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    faculty = db.relationship('ResearchFaculty', backref='research_area', lazy=True)
    journals = db.relationship('ResearchJournal', backref='research_area', lazy=True)
    conferences = db.relationship('ResearchConf', backref='research_area', lazy=True)

    def __repr__(self):
        return f"News('{self.title}')"

class ResearchFaculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('research.id'), nullable=False)

class ResearchJournal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('research.id'), nullable=False)

class ResearchConf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('research.id'), nullable=False)