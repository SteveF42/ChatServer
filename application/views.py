from flask import Flask, redirect, url_for, render_template, request, session, flash, Blueprint

view = Blueprint('views',__name__,static_folder='static')

@view.route('/')
def home():
    user = session.get('user',None)

    if user == None:
        return redirect(url_for('views.login'))
    else:
        return render_template('home.html', user=user)


@view.route('/login', methods=['POST','GET'])
def login(): 
    if request.method == "POST":
        user = request.form['input-text']
        if len(user) < 2:
            flash('Name must be longer than one character','info')
            return redirect(url_for('views.login'))
        else:
            session['user'] = user
            return redirect(url_for('views.home'))
    else:
        return render_template('login.html', context={'session':session})


@view.route('/logout',methods=['POST','GET'])
def logout():
    if 'user' in session:
        flash(f'You have been logged out {session["user"]}','info')
    session.pop('user',None)
    return redirect(url_for('views.home'))