from flask import Flask

app = Flask(__name__)

from url_shortener import routes