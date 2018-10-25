"""
Main module of the server file
"""

# 3rd party moudles

from flask import render_template
import connexion
from flask_cors import CORS

import logging

logging.basicConfig(level=logging.INFO)

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# add CORS support
CORS(app.app)

# create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
