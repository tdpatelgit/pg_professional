"""Main server file."""
import os
from datetime import timedelta, datetime
from flask import Flask, redirect, url_for, render_template, request, session, flash

template_dir = os.path.abspath('./src/templates')
app = Flask(__name__, template_folder=template_dir)

app.secret_key = 'AbCdEfG'
app.permanent_session_lifetime = timedelta(minutes=3)
auth_data = {'Tejas': 'abcd'}


@app.route('/')
@app.route('/home')
def home():
    """Home route."""
    return render_template('home.html')


@app.route('/guest')
def guest():
    """Gest route."""
    if 'user' in session:
        return render_template('welcome.html')

    return render_template('login.html')


@app.route('/admin')
def admin():
    """Admin route."""
    return render_template('admin.html')


@app.route('/rent')
def rent():
    """Rent route."""
    return render_template('rent.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Login route."""
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        code = request.form['pass']
        session['user'] = user
        session['code'] = code
        session['login_at'] = datetime.now()
        for username, password in auth_data.items():
            if session['user'] == username and session['code'] == password:
                flash('You have logged in successfully', 'info')
                return redirect(url_for('guest'))

        flash(['Invalid login credentials'])
        return render_template('login.html')

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout route."""
    if 'user' in session:
        session.pop('user', None)
        flash('You have logged out successfully', 'info')
        return render_template('home.html')

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
