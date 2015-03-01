from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'nickname':'Kushal'} # A fake user is being created
	return '''
	<html>
	<head>
		<title> Learning Flask </title>
	</head>

	<body>
		<h1> Hello World, this my first test with Flask.
		''' + user['nickname'] + '''</h1>
	</body>
	</html>
	'''
