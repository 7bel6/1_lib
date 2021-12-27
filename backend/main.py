from flask import Flask, jasonify
from flask_cors import CORS

# intialize the flask app
app = Flask(__name__)

# update the app
app.config.from_object(__name__)

# enable CORS
CORS(app, resouces={r'/*': {'origins': '*'}})
