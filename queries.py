# Average lap time of a driver for a given race (in seconds)
# driver found by driver id
# race found by race id
def find_average_laptime_by_race_id_and_driver_id(db_cursor, race_id, driver_id):
    query = f"select AVG(LAP.milliseconds)/1000 from LAP where race_id={race_id} and driver_id = {driver_id}"
    db_cursor.execute(query)



# Average lap time of a driver for a given race (in seconds)
# driver found by last name
# race found by race id
def find_average_laptime_by_race_id_and_driver_name(db_cursor, race_id, driver_surname):
    query = f"""select AVG(LAP.milliseconds)/1000 from LAP, DRIVERS where race_id={race_id} and DRIVERS.surname = "{driver_surname}" 
        AND DRIVERS.driver_id = LAP.driver_id"""
    db_cursor.execute(query)


# Average lap time of a driver FOR ALL RACES ON THAT CIRCUIT
# driver by driver surname
# circuit by circuit ref
def average_laptime_by_circuit(db_cursor, driver_surname, circuit_ref):
    query = f"""SELECT AVG(LAP.milliseconds)/1000
    FROM LAP, CIRCUITS, DRIVERS, RACES
    WHERE DRIVERS.surname = "{driver_surname}" AND DRIVERS.driver_id = LAP.driver_id AND
        RACES.circuit_id = CIRCUITS.circuit_id and LAP.race_id = RACES.race_id AND
        CIRCUITS.circuit_ref = '{circuit_ref}'"""
    db_cursor.execute(query)



# Average difference of laptimes of two drivers from a given race
# drivers found by driver id
# race found by race id
def average_pace_difference_by_race(db_cursor, first_driver_id, second_driver_id, race_id):
    query = f"""SELECT AVG(lap1.milliseconds - lap2.milliseconds) / 1000
    FROM LAP as lap1, LAP as lap2
    WHERE lap1.race_id = {race_id} AND lap2.race_id = {race_id} AND
        lap1.driver_id = {first_driver_id} and lap2.driver_id = {second_driver_id}"""
    db_cursor.execute(query)


# Average race results grouped by number of pit stops made for a race (this is for a single race)
# race determined by race id
def average_race_results_by_pitstop_single_race(db_cursor, race_id):
    query = f"""SELECT Pitstopcount, AVG(position_order)
    FROM (Select COUNT(*) as Pitstopcount, surname, position_order FROM PITSTOP, DRIVERS, RESULTS
    WHERE PITSTOP.driver_id = DRIVERS.driver_id AND RESULTS.driver_id = DRIVERS.driver_id AND
        PITSTOP.race_id = {race_id} AND RESULTS.race_id = PITSTOP.race_id
    GROUP BY DRIVERS.driver_id) as aggregates
    GROUP BY Pitstopcount
    HAVING Pitstopcount <= 4;"""
    db_cursor.execute(query)


# Average race results grouped by number of pit stops made for ALL RACES ON A CIRCUIT
# circuit determined by circuit ref
def average_race_results_by_pitstop_all_races_at_circuit(db_cursor, circuit_ref):
    query = f"""SELECT Pitstopcount, AVG(position_order)
    FROM (Select COUNT(*) as Pitstopcount, surname, position_order FROM PITSTOP, DRIVERS, RESULTS, CIRCUITS, RACES
    WHERE PITSTOP.driver_id = DRIVERS.driver_id AND RESULTS.driver_id = DRIVERS.driver_id AND
        RESULTS.race_id = PITSTOP.race_id AND RACES.circuit_id = CIRCUITS.circuit_id
        AND RACES.race_id = RESULTS.race_id AND CIRCUITS.circuit_ref = "{circuit_ref}"
    GROUP BY DRIVERS.driver_id) as aggregates
    GROUP BY Pitstopcount
    HAVING Pitstopcount <= 4"""
    db_cursor.execute(query)
