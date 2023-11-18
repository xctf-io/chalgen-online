from flask import Flask, render_template, request, redirect, url_for
from app_utilities import create_folder, create_empty_comp

app = Flask(__name__)

INIT_COMP = False

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/create")
def create():
	global INIT_COMP
	if (INIT_COMP == False):
		return render_template('initcomp.html')
	else:
		return render_template("create.html")

@app.route("/edithome")
def edithome():
	return render_template("edithome.html")

@app.route("/initcomp", methods=('GET', 'POST'))
def initcomp():


	# Check if comp has already been made, and if it has then dont allow access to initcomp again
	global INIT_COMP
	# if request.method == 'POST' and INIT_COMP == False:
	if request.method == 'POST':
		compname = request.form['compname']
		compauthor = request.form['compauthor']
		compskill = request.form['compskill']
		compdescription = request.form['compdescription']

		# Create empty comp
		create_empty_comp(compname,compauthor,compskill,compdescription)
		INIT_COMP = True
		return redirect(url_for('create'))
	else:
		return redirect(url_for('create'))

if __name__ == '__main__':
	app.run(debug=True)