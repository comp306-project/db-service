
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from app import cursor
import queries

app = Flask(__name__)
cors = CORS(app, resources={'/*':{'origins': 'http://localhost:3000'}}) 

from flask import current_app
print = lambda *args: current_app.logger.info(*args)

@app.route('/find_average_laptime_by_race_id_and_driver_id', methods=['POST'])
def find_average_laptime_by_race_id_and_driver_id():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    print(data, type(data))
    race_id, driver_id = float(data['race_id']), float(data['driver_id'])
    res = queries.find_average_laptime_by_race_id_and_driver_id(cursor, race_id, driver_id)
    return jsonify(res), 200


@app.route('/average_pace_difference_by_race', methods=['POST'])
def average_pace_difference_by_race():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    print(data, type(data))
    first_driver_id, second_driver_id, race_id = float(data['first_driver_id']), float(data['second_driver_id']), float(data['race_id'])
    res = queries.average_pace_difference_by_race(cursor, first_driver_id, second_driver_id, race_id)
    return jsonify(res), 200



@app.route('/average_race_results_by_pitstop_single_race', methods=['POST'])
def average_race_results_by_pitstop_single_race():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    race_id = float(data['race_id'])
    res = queries.average_race_results_by_pitstop_single_race(cursor, race_id)
    return jsonify(res), 200



@app.route('/average_race_results_by_pitstop_all_races_at_circuit', methods=['POST'])
def average_race_results_by_pitstop_all_races_at_circuit():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    circuit_ref = data['circuit_ref']
    res = queries.average_race_results_by_pitstop_all_races_at_circuit(cursor, circuit_ref)
    return jsonify(res), 200


@app.route('/find_countries_wins', methods=['POST'])
def find_countries_wins():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    position = float(data['position'])
    print(position)
    res = queries.find_countries_wins(cursor, position)
    print(res)
    return jsonify(res), 200


@app.route('/find_country_drivers', methods=['POST'])
def find_country_drivers():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    nationality = data['nationality']
    res = queries.find_country_drivers(cursor, nationality)
    return jsonify(res), 200

@app.route('/find_drivers_who_have_been_in_position', methods=['POST'])
def find_drivers_who_have_been_in_position():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    year = float(data['year'])
    res = queries.find_drivers_who_have_been_in_position(cursor, year)
    return jsonify(res), 200

@app.route('/average_pitstop_of_drivers', methods=['POST'])
def average_pitstop_of_drivers():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    race_id = float(data['race_id'])
    res = queries.average_pitstop_of_drivers(cursor, race_id)
    return jsonify(res), 200

@app.route('/average_position_of_drivers_ascend', methods=['POST'])
def average_position_of_drivers_ascend():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    race_year = float(data['race_year'])
    res = queries.average_position_of_drivers_ascend(cursor, race_year)
    return jsonify(res), 200

@app.route('/the_drivers_for_their_nationality', methods=['POST'])
def the_drivers_for_their_nationality():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    res = queries.the_drivers_for_their_nationality(cursor)
    return jsonify(res), 200


if __name__ == '__main__':
   app.run(host='0.0.0.0', port='5000', debug=True)





   
