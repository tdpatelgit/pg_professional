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
def route_home():
    """Home route."""
    logging.info('Route :: /')
    return render_template('home.html')


@app.route('/about')
def route_about():
    """About route."""
    logging.info('Route :: /about')
    return render_template('about.html')


@app.route('/amenities')
def route_amenities():
    """Amenities route."""
    logging.info('Route :: /amenities')
    return render_template('amenities.html')


@app.route('/packages')
def route_packages():
    """Package route."""
    logging.info('Route :: /packages')
    return render_template('packages.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    """Login route."""
    logging.info('Route :: /login %s', request.method)
    if request.method == 'POST':
        frm_user_name = request.form.get('user_name', '')
        frm_login_password = request.form.get('login_password', '')
        for auth_user_name, auth_login_password in auth_data.items():
            if frm_user_name == auth_user_name and frm_login_password == auth_login_password:
                session.permanent = True
                session['user'] = frm_user_name
                session['login_at'] = datetime.now()

                flash('You have logged in successfully', 'success')
                return redirect(url_for('route_home'))

        flash('Invalid login credentials, Please try again', 'danger')
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
