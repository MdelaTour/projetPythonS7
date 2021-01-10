from flask import (Flask, make_response, redirect, render_template, abort, url_for, session)
app = Flask(__name__)

@app.route('/hello')
def hello():
	return 'Hello, World!'

@app.route('/')
def root_url():
	# returned value = response
	return render_template("projetfinal.html")


if __name__ == '__main__':
	app.run(debug=True)