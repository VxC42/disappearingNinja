from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

@app.route('/')
def index():
    return "No ninjas here"

@app.route('/ninja')
def ninja():
    displayAll=True
    return render_template('ninja.html', displayAll=displayAll)

@app.route('/ninja/<color>')
def getColor(color):
    displayAll = False
    return render_template('ninja.html', color=color, displayAll=displayAll)



app.run(debug=True)
