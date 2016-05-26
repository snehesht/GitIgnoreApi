import os
import re

# Global Config
DATA_DIR = "../gitignore"
FILE_DOT_GITIGNORE_REGEX = "^.*\.gitignore$"
"""
	Class to access data
"""
class DataStore(object):
	"""docstring for DataStore"""
	def __init__(self):
		super(DataStore, self).__init__()
		self.data = {}
		self.load_files()

	"""
	Load files from data_dir with markdown format and return a map with key as filename and value as contents
	"""
	def load_files(self):
		print("loading files ...")
		data = {}
		# os.chdir(DATA_DIR)
		files_in_dir = os.listdir(DATA_DIR)
		for f in files_in_dir:
			# safegaurd to load only *.md files
			if re.match(FILE_DOT_GITIGNORE_REGEX,f) is not None:
				# Read each file and save it's content in a dict with key as filename and value as content
				with open(DATA_DIR+"/"+f) as fp:
						key = f.replace(".md","")
						value = fp.read()
						data[key] = value
		self.data = data

		if self.data == data:
			# :SUCCESS
			return True
		else:
			# :FAIL
			return False

	# Function to access data, this is usually called
	def get_data(self):
		return self.data

	# Reload data from DATA_DIR, usually called when changes are made
	def reload(self):
		try:
			self.load_files()
		except:
			print("Data reloading failed")