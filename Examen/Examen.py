from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("Tienda.html")

@app.route('/kungfupanda')
def kungfupanda():
	return render_template("Kung Fu Panda.html")

@app.route('/himym')
def himym():
	return render_template("How I Met Your Mother.html")

@app.route('/deadpool')
def deadpool():
	return render_template("Deadpool.html")

@app.route('/18')
def plus18():
	return render_template("+18.html")

@app.route('/integrantes')
def integrantes():
	return render_template("integrantes.html")

app.run(port=3000)