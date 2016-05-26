from flask import Flask
from mapfiles import DataStore

app = Flask(__name__)
ds = DataStore()
data = ds.get_data()

for key,val in data.items():
	print(key,len(val))