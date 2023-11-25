from flask import Flask, render_template, request, redirect, url_for
from app_utilities import *
import os

app = Flask(__name__)

if (not folder_occupied("competitions")):
	SELECTED_COMP = None
else:
	SELECTED_COMP = retrieve_first_comp()

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
		return redirect(url_for('edithome'))

@app.route("/edithome")
def edithome():
	global SELECTED_COMP
	if (SELECTED_COMP == None):
		return redirect(url_for('createcomp'))
	else:
		return render_template("edithome.html")
	
@app.route("/savehome", methods=('GET', 'POST'))
def savehome():
	if request.method == 'POST':
		saved_text = request.form['hometext']
		# sanitized_text = saved_text.replace('','\n')
		# overwrite_file(str(SELECTED_COMP)+'/Home.md',saved_text)
		sanitized_text = saved_text.replace('\r\n', '\n').replace('\r', '\n')  # Replace different newline formats
		print(saved_text)
		print(saved_text.count('\n'))
		overwrite_file(os.path.join('competitions',str(SELECTED_COMP),'Home.md'),sanitized_text)
	return redirect(url_for('edithome'))

@app.route("/selectcomp", methods=('GET', 'POST'))
def selectcomp():
	global SELECTED_COMP
	SELECTED_COMP = request.form['competitions']

	if (SELECTED_COMP == 'Select competition'):
		SELECTED_COMP = retrieve_first_comp()

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

@app.context_processor
def utility_processor():
	def get_home():
		return extract_text('competitions/'+str(SELECTED_COMP),'Home.md')
	return dict(get_home=get_home)

@app.context_processor
def utility_processor():
	def get_all_environments():
		return get_all_environments()
	return dict(get_all_environments=get_all_environments)

@app.context_processor
def utility_processor():
	def get_environments():
		return get_environments(SELECTED_COMP)
	return dict(get_environments=get_environments)

if __name__ == '__main__':
	app.run(debug=True)