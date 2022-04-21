"""Main server file."""
import os
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta, datetime

template_dir = os.path.abspath('./src/templates')
print(f'template_dir: {template_dir}')
app = Flask(__name__, template_folder=template_dir)

app.secret_key = 'AbCdEfG'
app.permanent_session_lifetime = timedelta(minutes=3)
nap = {'Tejas': 'abcd'}


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
        print('Login POST')
        session.permanent = True
        user = request.form['nm']
        code = request.form['pass']
        session['user'] = user
        session['code'] = code
        session['login_at'] = datetime.now()
        for n, p in nap.items():
            if session['code'] == p and session['user'] == n:
                flash('You have logged in successfully', 'info')
                return redirect(url_for('guest'))

        print('Invalid credentials')
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
