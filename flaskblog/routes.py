from flask import render_template,url_for,flash,redirect
from flaskblog import app,db,bcrypt
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm

posts = [
    {
        'name': 'Vishal',
        'title': 'person1',
        'DOB':  '31-05-2003',
        'matter': 'Hi Vishal you are born on 31st may 2003'
    },
    {
        'name': 'admin',
        'title': 'person2',
        'DOB':  '23-07-2003',
        'matter': 'Hi admin you are born on 23rd July 2003'
    }
]
@app.route("/") 
@app.route("/home")
def home():
    return render_template('home.html',dic=posts)
@app.route("/about") 
def about():
    return render_template('about.html',title='About')
@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit() 
        flash('Your account has been created! You are now able to log in','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)
@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You Have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html',title='Login',form=form)