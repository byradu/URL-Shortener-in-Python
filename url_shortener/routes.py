from url_shortener import app
from flask import render_template,request,flash


@app.route('/',methods = ['POST','GET'])
@app.route('/home/',methods = ['POST'])
def index():
    if request.method == 'POST':
        link = request.form['linkElement']
        if checkUrl == False:
            flash('Insert a running site')
            return render_template('index.html',data='')
        shortUrl = makeItShort(link)
        return render_template('index.html',data=shortUrl)
    return render_template('index.html',data='')

def checkUrl(link):
    import urllib.request
    statusCode = urllib.request.urlopen(link).getcode()
    print(statusCode)
    if statusCode == 200:
        return True
    return False

def makeItShort(link):
    import pyshorteners as shortener
    sh = shortener.Shortener()
    return sh.tinyurl.short(link)