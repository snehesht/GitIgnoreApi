from flask import Flask
from mapfiles import DataStore

api_app = Flask(__name__)
ds = DataStore()
data = ds.get_data()

from server import *
