from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(140))
    books = db.relationship('Book',backref = 'owner', lazy = 'dynamic')
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3
    def __repr__(self):
        return '<User %r>' % (self.username)

class Book(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) 
    isbn = db.Column(db.String(120))
    cover = db.Column(db.String(120))
    title = db.Column(db.String(120))
    author = db.Column(db.String(120))
    def __repr__(self):
        return '<Book %r>' % (self.isbn)
