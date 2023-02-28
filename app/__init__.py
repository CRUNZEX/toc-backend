from flask import Flask, render_template

app = Flask(__name__)

# Page: HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# Modules
from app.services import default, routes