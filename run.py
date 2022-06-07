
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import simplejson

from app import cursor
import queries

app = Flask(__name__)
cors = CORS(app, resources={'/*':{'origins': 'http://localhost:3000'}}) 

from flask import current_app
print = lambda *args: current_app.logger.info(*args)


@app.route('/circuits', methods=['GET'])
def circuits():
    query = 'SELECT circuit_ref FROM CIRCUITS'
    cursor.execute(query)
    res = cursor.fetchall()
    res = simplejson.dumps(res)
    return jsonify(res), 200

@app.route('/nationality', methods=['GET'])
def nationality():
    query = 'SELECT DISTINCT(nationality) FROM DRIVERS'
    cursor.execute(query)
    res = cursor.fetchall()
    res = simplejson.dumps(res)
    return jsonify(res), 200

@app.route('/get_driver_id', methods=['POST'])
def get_driver_id():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    surname, forename = data['surname'], data['forename']
    query = f"""SELECT driver_id
    FROM DRIVERS
    WHERE DRIVERS.surname = "{surname}" and DRIVERS.forename = "{forename}"
    """
    cursor.execute(query)
    res = cursor.fetchall()
    res = simplejson.dumps(res)
    return jsonify(res), 200

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


@app.route('/find_countries_all_wins', methods=['POST'])
def find_countries_all_wins():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    res = queries.find_countries_all_wins(cursor)
    return json.dumps(res, use_decimal=True)


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

@app.route('/find_countries_wins', methods=['POST'])
def find_countries_wins():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    position = float(data['position'])
    res = queries.find_countries_wins(cursor, position)
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

@app.route('/constructors_with_zero_points', methods=['POST'])
def constructors_with_zero_points():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    res = queries.constructors_with_zero_points(cursor)
    return jsonify(res), 200

@app.route('/best_drivers_from_best_constructors', methods=['POST'])
def best_drivers_from_best_constructors():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    won_count = float(data['won_count'])
    res = queries.best_drivers_from_best_constructors(cursor,won_count)
    return jsonify(res), 200

@app.route('/average_laptime_by_circuit', methods=['POST'])
def average_laptime_by_circuit():
    data = request.json
    if not type(data) == dict:
        data = json.loads(data)
    driver_surname = data['driver_surname']
    circuit_ref = data['circuit_ref']
    res = queries.average_laptime_by_circuit(cursor, driver_surname, circuit_ref)
    return jsonify(res), 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port='5000', debug=True)





   
