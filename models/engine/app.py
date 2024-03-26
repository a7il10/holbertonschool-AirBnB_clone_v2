from flask import Flask, jsonify
from db_storage import DBStorage

app = Flask(__name__)
db = DBStorage()

@app.route('/states', methods=['GET'])
def get_states():
    states = db.all('State')
    return jsonify({k: str(v) for k, v in states.items()})

@app.route('/cities', methods=['GET'])
def get_cities():
    cities = db.all('City')
    return jsonify({k: str(v) for k, v in cities.items()})

if __name__ == '__main__':
    app.run(debug=True)