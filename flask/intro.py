from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def fello():
	n = 'Taha'
	return render_template('ind.html', name = n)

app.run(debug = True)	