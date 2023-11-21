from flask import Flask, render_template, request, redirect, url_for
from app_utilities import create_folder, create_empty_comp, folder_occupied, list_all_comps

app = Flask(__name__)

SELECTED_COMP = None

@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html")

@app.route("/create")
def create():
	# Check if at least one competition has been made, if not then force them to initcomp
	if (not folder_occupied("competitions")):
		return redirect(url_for('createcomp'))
	else:
		return render_template("create.html")

@app.route("/edithome")
def edithome():
	return render_template("edithome.html")

@app.route("/selectcomp", methods=('GET', 'POST'))
def selectcomp():
	global SELECTED_COMP
	SELECTED_COMP = request.form['competitions']
	return redirect(url_for('create'))

@app.route("/initcomp", methods=('GET', 'POST'))
def initcomp():
	# Check if comp has already been made, and if it has then dont allow access to initcomp again
	# Decisions been made: user can create mutiple competitions if they want to. therefore initcomp can be called

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

@app.route("/createcomp", methods=('GET', 'POST'))
def createcomp():
	return render_template("initcomp.html")

@app.context_processor
def utility_processor():
	def list_comps():
		return list_all_comps()
	return dict(list_comps=list_comps)

@app.context_processor
def utility_processor():
	def get_selected_comp():
		return SELECTED_COMP
	return dict(get_selected_comp=get_selected_comp)

if __name__ == '__main__':
	app.run(debug=True)