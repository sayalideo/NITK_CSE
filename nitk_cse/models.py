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
        return f"Research('{self.title}')"

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

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    def __repr__(self):
        return f"Professor('{self.name}')"

class CSFY(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    csfy_file = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f"CSFY('{self.csfy_file}')"

class CSSY(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cssy_file = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f"CSSY('{self.cssy_file}')"

class ISFY(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isfy_file = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f"ISFY('{self.isfy_file}')"

class ISSY(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issy_file = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f"ISSY('{self.issy_file}')"
    
class RDProjects(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

class Consultancy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    guide = db.Column(db.String(100), nullable=False)
    agency = db.Column(db.String(100), nullable=False)
    student = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(10), nullable=False)