from flask import Flask

app = Flask(__name__)
'''
We need the secret key so we can flash a error message if the provided site doesn't work.
'''
app.config['SECRET_KEY'] = '59881a1df4e0753c15240d165e6a3fca02f8b855aaa1307fd2069cff8844aaaa'

from url_shortener import routes