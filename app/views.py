from app import app,db
from flask import request,redirect,url_for,render_template,session,flash,g
from forms import LoginForm,RegistrationForm,PostForm
from models import Books
from functools import wraps
from gbooks import bookinfo



@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")



@app.route('/register',methods = ["GET","POST"] )
def registration():
    return render_template("register.html",form =form)


@app.route('/user')
def user():
    books = Books.query.all()
    #info = bookinfo(books)
    return render_template('user.html',books = books )


@app.route('/add')
def add():
    binfo = bookinfo()
    for b in binfo:
        title,cover,author,category = b
        book = Books(title = title,cover = cover ,author = author,category = category)
        db.session.add(book)
        db.session.commit()
    return render_template("add.html")

@app.route('/post',methods = ['GET', 'POST'])
def userpost():
    form = PostForm()
    if form.validate_on_submit():
        isbn =form.isbn.data
        info = bookinfo(isbn)
        if  info !=None: 
            title,cover,author = info
            book = Books(isbn = isbn,title =title
                ,cover = cover,author = author)
            db.session.add(book)
            db.session.commit()
            flash("Your post is live")
            return redirect(url_for('user'))
    #books = Book.query.join(User).filter(User.username == username) 
    books = Books.query.all()
    return render_template('post.html',form=form)

@app.route('/login',methods = ["GET","POST"])
def login():
    return render_template("login.html",form=form)

