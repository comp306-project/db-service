import json
# Average lap time of a driver for a given race (in seconds)
# driver found by driver id
# race found by race id
def find_average_laptime_by_race_id_and_driver_id(db_cursor, race_id, driver_id):
    query = f"select AVG(LAP.milliseconds)/1000 from LAP where race_id={race_id} and driver_id = {driver_id}"
    db_cursor.execute(query)
    res = float(db_cursor.fetchall()[0][0])
    return json.dumps({'result' : res})


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
    

##=============OYA==============

# Showing every countries number of races they won
def find_countries_wins(db_cursor):
    query = f"""SELECT DRIVERS.nationality, COUNT(*) as TotalRaceWins FROM DRIVERS, RESULTS WHERE DRIVERS.driver_id=RESULTS.driver_id AND RESULTS.position_order = 1 
                GROUP BY DRIVERS.nationality ORDER BY COUNT(*) DESC"""
    db_cursor.execute(query)

# Showing a drivers name and surname for a selected country
def find_country_drivers(db_cursor, nationality):
    query = f"""SELECT DRIVERS.forename, DRIVERS.surname FROM DRIVERS WHERE DRIVERS.nationality = {nationality};"""
    db_cursor.execute(query)

# Showing drivers name and surname who
# have been in first specified positions in any race starting from a specified date 

def find_drivers_who_have_been_in_position(db_cursor, position, year):
    query = f"""SELECT DRIVERS.forename, DRIVERS.surname, DRIVERS.nationality FROM DRIVERS WHERE DRIVERS.driver_id IN 
        (SELECT DRIVERS.driver_id
        FROM DRIVERS,RESULTS,RACES
        WHERE DRIVERS.driver_id = RESULTS.driver_id AND RESULTS.position_order <{position} AND RESULTS.race_id=RACES.race_id  AND  RACES.race_id IN
            (SELECT RACES.race_id 
            FROM RACES
            WHERE RACES.year>{year}))"""

    db_cursor.execute(query)

# Showing total number of drivers from each country who
# never position as 1
def find_countries_wins(db_cursor, position):
    query = f"""SELECT DRIVERS.nationality, COUNT(*) as TotalDriverswhoNeverWon FROM DRIVERS WHERE DRIVERS.driver_id NOT IN 
	(SELECT DRIVERS.driver_id
	FROM DRIVERS,RESULTS
	WHERE DRIVERS.driver_id = RESULTS.driver_id AND RESULTS.position_order ={position})
    GROUP BY DRIVERS.nationality))""" 
    db_cursor.execute(query)  


   ##=============SEMA==============
#to find the average pitstop times of the drivers in the specified race
def average_pitstop_of_drivers(db_cursor, race_id):
    query = f"select DRIVERS.surname, AVG(PITSTOP.duration) from DRIVERS, PITSTOP where RACES.race_id = PITSTOP.race_id
             AND DRIVERS.driver_id = PITSTOP.driver_id AND RACES.race_id = PITSTOP.race_id AND RACES.race_id = {race_id}
             group by RACES.race_id, DRIVERS.driver_id"
    db_cursor.execute(query)
    res = float(db_cursor.fetchall()[0][0])
    return json.dumps({'result' : res})

#to find the average position of the drivers in the given year
def average_position_of_drivers_ascend(db_cursor, race_year):
     query = f"select AVG(RESULTS.position_order), DRIVERS.surname
                from DRIVERS, RESULTS, RACES
                where RACES.race_id = RESULTS.race_id AND RESULTS.race_id = RACES.race_id AND
                DRIVERS.driver_id = RESULTS.driver_id AND RACES.year = 2010
                group by DRIVERS.driver_id
                order by AVG(RESULTS.position_order) ASC"
     db_cursor.execute(query)
     res = float(db_cursor.fetchall()[0][0])
    return json.dumps({'result' : res})

#to find the driver names, surnames and the year they won
def the_drivers_for_their_nationality(db_cursor):
    query = f"select DISTINCT(DRIVERS.forename), DRIVERS.surname, RACES.year, DRIVERS.nationality, Constructors.nationality
              from DRIVERS, Constructors, RESULTS,RACES
              where DRIVERS.nationality = Constructors.nationality AND RESULTS.race_id = RACES.race_id AND
              RESULTS.constructor_id = Constructors.constructor_id AND DRIVERS.driver_id = RESULTS.driver_id AND 
              DRIVERS.driver_id IN (select DISTINCT(DRIVERS.driver_id) from DRIVERS, RESULTS, RACES
              where RESULTS.position_order = 1 AND RESULTS.race_id = RACES.race_id AND RESULTS.driver_id = DRIVERS.driver_id)"
    db_cursor.execute(query)
    res = float(db_cursor.fetchall()[0][0])
    return json.dumps({'result' : res})



if __name__ == '__main__':
    from app import cursor
    res = find_average_laptime_by_race_id_and_driver_id(cursor, 1009, 1)
    print(res)

