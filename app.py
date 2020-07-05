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
    data = request.form.get('entry')
    print(data)
    return render_template('index.html', result = data)






#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;1
    app.run('127.0.0.1', 4000, True)
