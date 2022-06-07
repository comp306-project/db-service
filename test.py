import requests
import json

base_url = f'http://localhost:5000/'

r = requests.post(f'{base_url}/find_average_laptime_by_race_id_and_driver_id', json={'race_id' : 1009, 'driver_id' : 1})
print(r.json())

r = requests.post(f'{base_url}/average_race_results_by_pitstop_all_races_at_circuit', json={'circuit_ref' : "Istanbul Park"})
print(r.json())

r = requests.post(f'{base_url}/average_pace_difference_by_race', json={'first_driver_id' : 1, "second_driver_id": 783, 'race_id': 1000})
print(r.json())

r = requests.post(f'{base_url}/average_race_results_by_pitstop_single_race', json={'race_id': 1000})
print(r.json())

r = requests.post(f'{base_url}/find_countries_all_wins')
print(r.json())

r = requests.post(f'{base_url}/find_country_drivers', json={'nationality': 'British'})
print(r.json())

r = requests.post(f'{base_url}/find_drivers_who_have_been_in_position', json={'year': '2014'})
print(r.json())

r = requests.post(f'{base_url}/find_countries_wins', json={'position': '1'})
print(r.json())

r = requests.post(f'{base_url}/average_pitstop_of_drivers', json={'race_id' : 1002})
print(r.json())

r = requests.post(f'{base_url}/the_drivers_for_their_nationality')
print(r.json())

r = requests.post(f'{base_url}/average_position_of_drivers_ascend', data={'year': '2014'})
print(r.json())

r = requests.post(f'{base_url}/constructors_with_zero_points')
print(r.json())

r = requests.post(f'{base_url}/best_drivers_from_best_constructors', data={'won_count': '3'})
print(r.json())

r = requests.post(f'{base_url}/average_laptime_by_circuit',data={'driver_surname': 'Hamilton','circuit_ref': 'Istanbul Park'})
print(r.json())





