# FLASK ES UN FRAMEWOR APPS WEB (BACKEND-SERVIDOR) PYTOHN
# SERVIDOR
# RESPONDE
# HOGAR/PUNTO DE INICIO -> HOST
# VENTANILLA/PUERTA -> PORT
# SERVIDOR -> DIRECCIÓN = HOST:PORT4
# IP -> *NUMERO* (HOST)
# LOCALHOST (127.0.0.1)
# PUERTO ESTANDAR (HTTP/HTTPS): 80
# PUERTO DIFERENTE -> 3000, 5000, 6969, 8000, 8001, 8008

import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
	return "<h1> Que pedo </h1><br><button> Que pedo de que wey?</button>"
@app.route('tacos', methods=['GET'])
app.run()