import os
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta, date, datetime

template_dir = os.path.abspath('./src/templates')
print(f'template_dir: {template_dir}')
app = Flask(__name__, template_folder=template_dir)

app.secret_key = "AbCdEfG"
app.permanent_session_lifetime = timedelta(minutes=3)
nap = {'Tejas':'abcd'}

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/guest")
def guest():
	if "user" in session:
		name = session["user"]
		today = date.today()
		d = today.strftime("%d")
		M = today.strftime("%B")
		Y = today.strftime("%Y")
		D = str(datetime.today().strftime('%A'))
		return render_template("welcome.html", name = name, d = d, D = D[:3], M = M[:3], Y = Y)
	else:
		return render_template("login.html")

@app.route("/admin")
def admin():
	return render_template("admin.html")

@app.route("/rent")
def rent():
	return render_template("rent.html")

@app.route("/login", methods = ['POST', 'GET'])
def login():
	if request.method == "POST":
		print('Login POST')
		session.permanent = True
		user = request.form["nm"]
		code = request.form["pass"]
		session["user"] = user
		session["code"] = code
		for n,p in nap.items() :
			if session["code"] == p and session["user"] == n:
				flash("You have logged in successfully", "info")
				return redirect(url_for("guest"))

		print('Invalid credentials')
		flash(["Invalid login credentials"])
		return render_template("login.html")
	else:
		return render_template("login.html")


@app.route("/logout")
def logout():
	if "user" in session:
		session.pop("user", None)
		flash("You have logged out successfully", "info")
		return render_template("home.html")
	else:
		return render_template("home.html")

if __name__ == '__main__':
	app.run(debug=True)