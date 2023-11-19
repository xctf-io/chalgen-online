from flask import Flask, render_template, request, redirect, url_for
from app_utilities import create_folder, create_empty_comp, folder_occupied

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html")

@app.route("/create")
def create():
	if (folder_occupied("competitions")):
		return render_template('initcomp.html')
	else:
		return render_template("create.html")

@app.route("/edithome")
def edithome():
	return render_template("edithome.html")

@app.route("/initcomp", methods=('GET', 'POST'))
def initcomp():


	# Check if comp has already been made, and if it has then dont allow access to initcomp again

	# Decisions been made: user can create mutiple competitions if they want to

	# if request.method == 'POST' and COMP_EXISTS == False:
	if request.method == 'POST':
		compname = request.form['compname']
		compauthor = request.form['compauthor']
		compskill = request.form['compskill']
		compdescription = request.form['compdescription']

		# Create empty comp
		create_empty_comp(compname,compauthor,compskill,compdescription)
		return redirect(url_for('create'))
	else:
		return redirect(url_for('create'))

if __name__ == '__main__':
	app.run(debug=True)