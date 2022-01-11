from flask import Flask, jsonify

from flask_cors import CORS

# intialize the flask app
app = Flask(__name__)

# update the app
app.config.from_object(__name__)

# enable CORS
CORS(app, resouces={r'/*': {'origins': '*'}})

# route to the index page


@app.route('/', methods=['GET'])
def greeting():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
