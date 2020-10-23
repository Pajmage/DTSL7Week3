from flask import Flask

app = Flask(__name__)

@app.route('/')
def easyDoesIt():
    return "<h1>Easy does it!</h1>"

if __name__ == '__main__':
    app.run()
