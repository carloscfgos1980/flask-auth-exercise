import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        secret_password = hash_password(password)

        for key, value in get_users().items():
            if key != username:
                return "This user does not exist"
            elif key == username and value != secret_password:
                return redirect(url_for('login', error=True))
            else:
                return render_template("dashboard.html", title="dashboard")

    return render_template("login.html", title="Log in")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('username')
    return redirect(url_for('index'))


def sign_out():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
