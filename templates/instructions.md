## INSTRUCTIONS

Step 1: Log In
Implement the specification of /login according to this table.

Method	Path	Response
GET	/login	A login page with a form that can be submitted. Endpoint for the form obtained from GET /login that logs the user in. For a succesful login, it redirects to /dashboard. Otherwise it redirects to /login?error=True. 
POST	/login

Tip:

use redirect(url_for('login', error=True)) to redirect back to the login page with an extra error parameter. Your only job, then, is to check for this query parameter on a GET request to /login and modify the page accordingly.

To help you along, we implemented two functions in helpers.py: 
bullet
hash_password: this takes a string (str) and returns the hashed version of that string.
bullet
get_users: takes no arguments and returns a dictionary where the keys are all the known usernames and the matching values are hashed versions of their password. We have two users in our database:

Alice with password secret
Bob with password supersecret

Step 2: Log out
Implement the functionality that whenever there is a GET or POST request to the path /logout, the user is logged out. This means that if present, the 'username' entry in their session dictionary is removed.

After being logged out, the user should be redirected to /.
Step 3: Dashboard
At the path /dashboard (responding to GET requests), create a dashboard that displays different content depending on which user visits it. Keep it simple! The exercise is about authentication, so the main objective here is to make it so that each user sees something different.
bullet
Be sure to at least display a customized greeting on this (fictional) user dashboard.
bullet
Consider adding some extra customized content by using Jinja's {% if %} -{% else %} blocks. More on that here(opens in a new tab).