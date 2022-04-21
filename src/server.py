"""Main server file."""
import os
import logging
from datetime import timedelta, datetime
from flask import Flask, redirect, url_for, render_template, request, session, flash

from src.utils import setup_log

setup_log(__file__)

template_dir = os.path.abspath('./src/templates')
app = Flask(__name__, template_folder=template_dir)

app.secret_key = 'AbCdEfG'
app.permanent_session_lifetime = timedelta(minutes=3)
auth_data = {'Tejas': 'abcd'}


@app.route('/')
@app.route('/home')
def home():
    """Home route."""
    logging.info('Route :: / or /home')
    return render_template('home.html')


@app.route('/guest')
def guest():
    """Gest route."""
    logging.info('Route :: /guest')
    if 'user' in session:
        return render_template('welcome.html')

    return render_template('login.html')


@app.route('/admin')
def admin():
    """Admin route."""
    logging.info('Route :: /admin')
    return render_template('admin.html')


@app.route('/rent')
def rent():
    """Rent route."""
    logging.info('Route :: /rent')
    return render_template('rent.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Login route."""
    logging.info('Route :: /login %s', request.method)
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
    logging.info('Route :: /logout')
    if 'user' in session:
        session.pop('user', None)
        flash('You have logged out successfully', 'info')
        return render_template('home.html')

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
