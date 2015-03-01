from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'nickname':'Kushal'} # A fake user is being created
	posts = [ # Fake posts
		{
			'author':{'nickname':'Kushal'},
			'body': 'Learning to Use Flask'
		},
		{
			'author':{'nickname':'AnotherUser'},
			'body': 'What a way to learn Flask'
		}
	]

	return render_template("index.html",
							title='Home',
							user=user,
							posts=posts)