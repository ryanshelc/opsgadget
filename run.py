from flask import Flask
from flask import render_template
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)