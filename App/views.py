from . import api_app
from . import data
from flask import request,render_template,jsonify
from flask import redirect, url_for
from collections import OrderedDict

@api_app.route('/')
def index_page():
	# tmpdata = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
	tmpdata = sorted([key for key in data])
	return render_template('index.html', data=tmpdata)

@api_app.route('/favicon.ico')
def favicon():
	return redirect(url_for('static', filename="facicon.ico"))

@api_app.route('/<file_name>')
def raw_gitignore_file(file_name):
	if file_name in data:
		return data[file_name]
	else:
		return '.gitignore for '+file_name+' not found'

@api_app.route('/view/<file_name>')
def fetch_gitignore_file(file_name):
	if file_name in data:
		return render_template('single.html', pkg_name=file_name,pkg=data[file_name].replace("\n","<br />"))
	else:
		return '.gitignore for '+file_name+' not found'