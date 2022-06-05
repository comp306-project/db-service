
from flask import Flask, jsonify, request
from app import cursor
import queries

app = Flask(__name__)

@app.route('/databases')
def databases():
    cursor.execute("SHOW DATABASES")
    result = [res[0] for res in cursor.fetchall()]
    return jsonify(result), 200

@app.route('/tables')
def tables():
    cursor.execute("SHOW TABLES")
    result = [res[0] for res in cursor.fetchall()]
    return jsonify(result), 200

@app.route('/tables/CIRCUITS')
def CIRCUITS():
    cursor.execute("SELECT * FROM CIRCUITS")
    result = {res[0] : [row for row in res[1:]] for res in cursor.fetchall()}
    return jsonify(result), 200


@app.route('/find_average_laptime_by_race_id_and_driver_id', methods=['POST'])
def find_average_laptime_by_race_id_and_driver_id():
    data = request.form
    race_id, driver_id = float(data['race_id']), float(data['driver_id'])
    res = queries.find_average_laptime_by_race_id_and_driver_id(cursor, race_id, driver_id)
    return jsonify(res), 200


@app.route('/average_race_results_by_pitstop_all_races_at_circuit', methods=['POST'])
def average_race_results_by_pitstop_all_races_at_circuit():
    data = request.form
    circuit_ref = str(data['circuit_ref'])
    res = queries.find_average_laptime_by_race_id_and_driver_id(cursor, circuit_ref)
    return jsonify(res), 200


@app.route('/average_pace_difference_by_race', methods=['POST'])
def average_pace_difference_by_race():
    data = request.form
    first_driver_id, second_driver_id, race_id = float(data['first_driver_id']), float(data['second_driver_id'], float(data['race_id']))
    res = queries.average_pace_difference_by_race(cursor, first_driver_id, second_driver_id, race_id)
    return jsonify(res), 200



@app.route('/average_race_results_by_pitstop_single_race', methods=['POST'])
def average_race_results_by_pitstop_single_race():
    data = request.form
    race_id = float(data['race_id'])
    res = queries.average_pace_difference_by_race(cursor, race_id)
    return jsonify(res), 200



@app.route('/average_race_results_by_pitstop_all_races_at_circuit', methods=['POST'])
def average_race_results_by_pitstop_all_races_at_circuit():
    data = request.form
    circuit_ref = data['circuit_ref']
    res = queries.average_race_results_by_pitstop_all_races_at_circuit(cursor, circuit_ref)
    return jsonify(res), 200



@app.route('/find_countries_wins', methods=['POST'])
def find_countries_wins():
    data = request.form
    res = queries.find_countries_wins(cursor)
    return jsonify(res), 200


@app.route('/find_country_drivers', methods=['POST'])
def find_country_drivers():
    data = request.form
    nationality = data['nationality']
    res = queries.find_country_drivers(cursor, nationality)
    return jsonify(res), 200

@app.route('/find_drivers_who_have_been_in_position', methods=['POST'])
def find_drivers_who_have_been_in_position():
    data = request.form
    year = float(data['year'])
    res = queries.find_drivers_who_have_been_in_position(cursor, year)
    return jsonify(res), 200


@app.route('/find_countries_wins', methods=['POST'])
def find_countries_wins():
    data = request.form
    position = float(data['position'])
    res = queries.find_countries_wins(cursor, position)
    return jsonify(res), 200


if __name__ == '__main__':
   app.run(host='0.0.0.0', port='5000', debug=True)





   
