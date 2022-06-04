# Average lap time of a driver for a given race (in seconds)
# driver found by driver id
# race found by race id
select AVG(LAP.milliseconds)/1000 from LAP where race_id=1009 and driver_id = 1;

# Average lap time of a driver for a given race (in seconds)
# driver found by last name
# race found by race id
select AVG(LAP.milliseconds)/1000 from LAP, DRIVERS where race_id=1009 and DRIVERS.surname = "Hamilton" AND DRIVERS.driver_id = LAP.driver_id;

# Average lap time of a driver FOR ALL RACES ON THAT CIRCUIT
# driver by driver id
# circuit by circuit ref
SELECT AVG(LAP.milliseconds)/1000
FROM LAP, CIRCUITS, DRIVERS, RACES
WHERE DRIVERS.surname = "Hamilton" AND DRIVERS.driver_id = LAP.driver_id AND
      RACES.circuit_id = CIRCUITS.circuit_id and LAP.race_id = RACES.race_id AND
      CIRCUITS.circuit_ref = "Istanbul Park";


# Average difference of laptimes of two drivers from a given race
# drivers found by driver id
# race found by race id
SELECT AVG(lap1.milliseconds - lap2.milliseconds) / 1000
FROM LAP as lap1, LAP as lap2
WHERE lap1.race_id = 1009 AND lap2.race_id = 1009 AND
      lap1.driver_id = 1 and lap2.driver_id = 830;



# Average race results grouped by number of pit stops made for a race
# race determined by race id
SELECT Pitstopcount, AVG(position_order)
FROM (Select COUNT(*) as Pitstopcount, surname, position_order FROM PITSTOP, DRIVERS, RESULTS
WHERE PITSTOP.driver_id = DRIVERS.driver_id AND RESULTS.driver_id = DRIVERS.driver_id AND
      PITSTOP.race_id = 901 AND RESULTS.race_id = PITSTOP.race_id
GROUP BY DRIVERS.driver_id) as aggregates
GROUP BY Pitstopcount
HAVING Pitstopcount <= 4;

# Average race results grouped by number of pit stops made for ALL RACES ON A CIRCUIT
# circuit determined by circuit ref
SELECT Pitstopcount, AVG(position_order)
FROM (Select COUNT(*) as Pitstopcount, surname, position_order FROM PITSTOP, DRIVERS, RESULTS, CIRCUITS, RACES
WHERE PITSTOP.driver_id = DRIVERS.driver_id AND RESULTS.driver_id = DRIVERS.driver_id AND
     RESULTS.race_id = PITSTOP.race_id AND RACES.circuit_id = CIRCUITS.circuit_id
    AND RACES.race_id = RESULTS.race_id AND CIRCUITS.circuit_ref = "Istanbul Park"
GROUP BY DRIVERS.driver_id) as aggregates
GROUP BY Pitstopcount
HAVING Pitstopcount <= 4;

# List winners of a circuit in descending order by date
SELECT drivers.forename, drivers.surname,
        races.name, races.date, results.position_order
        FROM results
        JOIN drivers ON results.driver_id = drivers.driver_id
        JOIN races ON results.race_id = races.race_id
        WHERE results.position_order = 1 AND
        RACES.circuit_id = 5
        ORDER BY date DESC ;



# Cumulative points of drivers (all time points)
# in descending order
# Top 10 most point scorers
SELECT drivers.forename, drivers.surname, drivers.nationality, SUM(results.points)
        FROM drivers
        JOIN results ON drivers.driver_id = results.driver_id
        GROUP BY drivers.driver_id
        ORDER BY SUM(results.points) DESC
        LIMIT 10;


# List all wins of a driver
# driver determined by name and surname
SELECT  DRIVERS.forename, surname, races.name, races.date, results.position_order
        FROM RESULTS, DRIVERS, RACES
        WHERE results.position_order = 1 AND drivers.surname = "Hamilton"
        AND forename = "Lewis" AND RESULTS.race_id = RACES.race_id AND RESULTS.driver_id = DRIVERS.driver_id
        ORDER BY date DESC ;


# Average qualifying result of a driver for a given circuit
# circuit determined by circuit ref
# driver determined by first and lastname
SELECT AVG(position), circuit_ref
FROM QUALIFYING, CIRCUITS, RACES, DRIVERS
WHERE QUALIFYING.race_id = RACES.race_id AND circuit_ref = "Circuit de Barcelona-Catalunya"
AND RACES.circuit_id = CIRCUITS.circuit_id AND QUALIFYING.driver_id = DRIVERS.driver_id
AND DRIVERS.forename = "Lewis" AND DRIVERS.surname = "Hamilton";

# Average qualifying result of a driver for a given circuit
# circuit determined by circuit ref
# driver determined by driver_id
SELECT AVG(QUALIFYING.position), circuit_ref
FROM QUALIFYING, CIRCUITS, RACES, DRIVERS
WHERE QUALIFYING.race_id = RACES.race_id AND circuit_ref = "Circuit de Barcelona-Catalunya"
AND RACES.circuit_id = CIRCUITS.circuit_id AND QUALIFYING.driver_id = DRIVERS.driver_id
AND DRIVERS.driver_id = 1;

# Average Qualifying result in a season
# season determined by year
# driver determined by id
SELECT AVG(QUALIFYING.position), DRIVERS.forename, DRIVERS.surname
FROM QUALIFYING, RACES, DRIVERS
WHERE QUALIFYING.race_id = RACES.race_id AND DRIVERS.driver_id = QUALIFYING.driver_id
AND RACES.year = 2016 AND DRIVERS.driver_id = 1;



# =============== OYA ===============
# Showing every countries
# number of races they won
SELECT DRIVERS.nationality, COUNT(*) as TotalRaceWins
FROM DRIVERS, RESULTS
WHERE DRIVERS.driver_id=RESULTS.driver_id AND RESULTS.position_order = 1
GROUP BY DRIVERS.nationality
ORDER BY COUNT(*) DESC;



# Showing a drivers name and surname for
# a selected country
SELECT DRIVERS.forename, DRIVERS.surname
FROM DRIVERS
WHERE DRIVERS.nationality = "British";



# ==========SEMA==============
SELECT AVG(PITSTOP.duration), DRIVERS.surname
FROM DRIVERS, PITSTOP, RACES
WHERE RACES.race_id = PITSTOP.race_id AND DRIVERS.driver_id = PITSTOP.driver_id AND RACES.race_id = PITSTOP.race_id AND RACES.race_id = 1000
GROUP BY RACES.race_id, DRIVERS.driver_id;


SELECT AVG(RESULTS.position_order), DRIVERS.surname
FROM DRIVERS, RESULTS, RACES
WHERE RACES.race_id = RESULTS.race_id AND RESULTS.race_id = RACES.race_id AND DRIVERS.driver_id = RESULTS.driver_id AND RACES.year = 2010
GROUP BY DRIVERS.driver_id
ORDER BY AVG(RESULTS.position_order) ASC ;

SELECT DISTINCT(DRIVERS.forename), DRIVERS.surname, RACES.year, DRIVERS.nationality, Constructors.nationality
FROM DRIVERS, Constructors, RESULTS,RACES
WHERE DRIVERS.nationality = Constructors.nationality AND RESULTS.race_id = RACES.race_id AND 
RESULTS.constructor_id = Constructors.constructor_id AND DRIVERS.driver_id = RESULTS.driver_id AND DRIVERS.driver_id IN 
(SELECT DISTINCT(DRIVERS.driver_id)
FROM DRIVERS, RESULTS, RACES
WHERE RESULTS.position_order = 1 AND RESULTS.race_id = RACES.race_id AND RESULTS.driver_id = DRIVERS.driver_id)


# ======== ATA============
### Q1
# The teams that haven't scored a point with their name, nat, best end position,
 # first race year and last race year
SELECT Co.name as TeamName, Co.nationality as Nationality, min(Re.position_order) as BestPosition, min(Ra.year), max(Ra.year)
FROM Constructors as Co, Results as Re, Races as Ra
WHERE Co.constructor_id = Re.constructor_id and Ra.race_id = Re.race_id
GROUP BY Co.constructor_id
having SUM(Re.points) = 0;


SELECT D.forename, D.surname, sum(Re.points) as TotalPoints
FROM Constructors as Co, Results as Re, Drivers as D
WHERE Co.constructor_id = Re.constructor_id
and D.driver_id = Re.driver_id
and Co.constructor_id in (
SELECT Co.constructor_id
FROM Constructors as Co, Results as Re
WHERE Co.constructor_id = Re.constructor_id and Re.position_order = 1
group by Co.constructor_id
having count(*) > 100
)
group by D.driver_id
order by sum(Re.points) dESC;


