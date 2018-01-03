from flask import Flask
import requests
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World! from flask2'

@app.route('/flask2')
def flask1():
	return 'I am flask 2'

@app.route('/greeting')
def greeting():
	r = requests.get('http://flask1/hello')	
	return r.text

@app.route('/')
def root():
	return 'Root index'

if __name__ == '__main__':
    app.run('0.0.0.0',5000)
