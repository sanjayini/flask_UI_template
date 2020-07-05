#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, url_for, request
import requests
import random
import os.path
import os
import random


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    return render_template('index.html', result = {'1' : '2'})


@app.route('/', methods=['GET','POST'])
def index():
    if (request.method == 'GET') :
        return render_template('index.html')
    data = request.form.get('content')
    print(data)
    res = get_sentiment_analysis(data)
    # res = make_response(json.dumps(res, ensure_ascii=False))
    # res.headers["Content-Type"] = "application/json; charset=utf-8"
    print(res.get('highlighted_content'))
    return render_template('index.html', result=res.get('highlighted_content'))




#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;1
    app.run('127.0.0.1', 4000, True)
