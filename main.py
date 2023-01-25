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

        for username in get_users():
            if username == get_users().keys():
                print("username exist")
                if secret_password == get_users().values():
                    print("success")
                    return redirect(url_for('dashboard'))

            else:
                raise "username is wrong"

    return render_template("login.html", title="Log in")


@app.route("/dashboard")
def dashboard():
    # YOUR SOLUTION HERE
    pass


@app.route("/logout", methods=["GET", "POST"])
def logout():
    # YOUR SOLUTION HERE
    pass


if __name__ == '__main__':
    app.run(debug=True)
