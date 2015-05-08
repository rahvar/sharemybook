from app import app,db,lm
from flask import request,redirect,url_for,render_template,session,flash,g
from flask.ext.login import login_user, logout_user, current_user
from forms import LoginForm,RegistrationForm,PostForm
from models import User,Book
from functools import wraps
from gbooks import bookinfo

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login_page'))

    return wrap

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")



@app.route('/register',methods = ["GET","POST"] )
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Thanks for registering!")
        
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(username = username,email= email,password=password)
   
        db.session.add(user)
        db.session.commit()
  
        session['logged_in'] = True
        session['username'] = username
       
        return  redirect(url_for('user',username = username))
 
    return render_template("register.html", form = form)

@app.route('/user/<username>',methods = ['GET', 'POST'])
@login_required
def user(username):
    form = PostForm()
    user = User.query.filter_by(username = username).first()
    if user is None:
        flash('User %s not found.' % username)
        return redirect(url_for('home'))
    if form.validate_on_submit():
            book = Book(isbn = form.isbn.data,owner = user)
            db.session.add(book)
            db.session.commit()
            flash("Your post is live")
            return redirect(url_for('user',username = username))
    #books = Book.query.join(User).filter(User.username == username)  
    books = user.books.all()
    #info = bookinfo(books)
    return render_template('user.html',username=username,user=user ,form=form,books =books)

@app.route('/login',methods = ["GET","POST"])
def login():
    form = LoginForm()
    error = ''
    if 'logged_in' in session:
        return redirect(url_for('user',username = session['username'])) 
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
      
            if user.password == form.password.data:
        
                session['logged_in'] = True
                session['username'] = username
                flash("logged in")
                return redirect(url_for('user',username = username))
            else:
                error = "Incorrect password"    
        else:
            error = "Invalid credentials, try again"
    return render_template("login.html",form=form,error = error)

@app.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('home'))