# Exercise auth notes

* I added a functionality so I can run the program from the VSC:
if __name__ == '__main__':
    app.run(debug=True)

* This are the username and password to test the app:
username:Alice, password: secret
username:Bob, password: supersecret

* No funcking clue what this is for:
def sign_out():
    return redirect(url_for('index'))

* I applied the sections thing but also didn't make any sense without creating a proper database which I already know to do with SQLAlquemy