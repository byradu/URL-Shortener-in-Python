from os import error
import urllib.request
from flask.helpers import url_for
import pyshorteners as shortener
from werkzeug.utils import redirect
from url_shortener import app
from flask import render_template,request,flash

recent_history = list()
already_computed = dict()

@app.route('/',methods = ['POST','GET'])
@app.route('/home/',methods = ['POST','GET'])
def index():
    '''
    Returns to the client the blank homepage, 
    the homepage with an error message if the link is bad or the homepage with a shorter link.
    
    '''
    global recent_history,already_computed
    if request.method == 'POST':
        link = request.form['linkElement']
        
        if link in already_computed:
            return render_template('index.html',data=already_computed[link],recent_history=recent_history)

        recent_history = recent_history[::-1]
        
        if check_url(link) == False: 
            return render_template('index.html',some_error = True,provided_link = link,recent_history=recent_history)
        
        short_url = make_it_short(link)
        
        already_computed[link] = short_url #just to not compute a new link everytime
        recent_history.append((link,short_url))
        recent_history = recent_history[::-1]
        if len(recent_history) > 10:
            recent_history = recent_history[:10]
        
        return render_template('index.html',data=short_url,recent_history=recent_history)
    return render_template('index.html',data='',recent_history=recent_history)


def check_url(link):
    '''
    Checks if the client provides a valid URL.
    '''
    try:
        statusCode = urllib.request.urlopen(link)
    except Exception as e:
        print(str(e))
        return False
    else:
        if statusCode.getcode() < 400:
            return True
        return False


def make_it_short(link):
    '''
    Return a smaller version of the link using one of the APIs available.
    More info at: https://pyshorteners.readthedocs.io/en/latest/
    '''
    try:
        sh = shortener.Shortener()
    except Exception as e:
        print( str(e) )
    else:
        return sh.tinyurl.short(link)