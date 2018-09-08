import requests

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/pokemon/<int:id>/', methods=['GET'])
def getPokemonId(id):
	url = "http://pokeapi.co/api/v2/pokemon/" + str(id)
	r = requests.get(url)
	data = r.json()
	name = data["name"]
	return render_template('index1.html', **locals())


@app.route('/pokemon/<string:name>/', methods=['GET'])
def getPokemonName(name):
	url = "http://pokeapi.co/api/v2/pokemon/" + name
	r = requests.get(url)
	data = r.json()
	id = data["id"]
	name = name.title()
	return render_template('index2.html', **locals())




if __name__ == '__main__':
    app.run()
