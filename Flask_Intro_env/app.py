
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_func():
    users = ["Paj", "Ray", "Mick"]
    return render_template('index.html', title = "Flask Example", users = users)

@app.route('/test_route')
def my_func_2():
    return "<h2>Flask App - Debug True from test route</h2>"

app.run(debug=True)