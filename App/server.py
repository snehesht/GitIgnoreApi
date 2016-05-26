from __init__ import api_app
from __init__ import data
from flask import request,render_template

@api_app.route('/')
def index_page():
	return "Welcome..."

@api_app.route('/<file_name>')
def fetch_gitignore_file(file_name):
	if file_name in data:
		return data[file_name]
	else:
		return '.gitignore for '+file_name+' not found'