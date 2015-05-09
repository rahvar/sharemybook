from app import db

class Books(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    isbn = db.Column(db.String(120))
    cover = db.Column(db.String(120))
    title = db.Column(db.String(120))
    author = db.Column(db.String(120))
    category = db.Column(db.String(120))
    def __repr__(self):
        return '<Books %r>' % (self.isbn)
