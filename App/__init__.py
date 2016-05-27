from flask import Flask
from . import mapfiles

api_app = Flask(__name__)
ds = mapfiles.DataStore()
data = ds.get_data()

from . import views
