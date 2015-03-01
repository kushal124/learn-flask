from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'nickname':'Kushal'} # A fake user is being created
	return render_template('index.html',user=user)
