from flask import Flask
from flask import render_template, url_for
import os

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Surprize Quiz.html')
#if __name__ == '__main__':
#    app.run(host='localhost', port=8000, debug=True)

port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=port, debug=True)