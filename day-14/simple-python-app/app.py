from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/surya')
def hello():
    return 'Hello, Surya!'

if __name__ == '__main__':
    app.run()
