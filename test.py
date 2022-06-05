import requests


base_url = f'http://localhost:5000/'

r = requests.post(f'{base_url}/find_average_laptime_by_race_id_and_driver_id', data={'race_id' : 1009, 'driver_id' : 1})
print(r.json())

r = requests.post(f'{base_url}/average_race_results_by_pitstop_all_races_at_circuit', data={'circuit_ref' : "Istanbul Park"})
print(r.json())

r = requests.post(f'{base_url}/average_pace_difference_by_race', data={'first_driver_id' : 1, "second_driver_id": 783, 'race_id': 1000})
print(r.json())

r = requests.post(f'{base_url}/average_race_results_by_pitstop_single_race', data={'race_id': 1000})
print(r.json())

r = requests.post(f'{base_url}/average_race_results_by_pitstop_all_races_at_circuit', data={'circuit_ref': 'Istanbul Park'})
print(r.json())

r = requests.post(f'{base_url}/find_countries_wins')
print(r.json())

r = requests.post(f'{base_url}/find_country_drivers', data={'nationality': 'British'})
print(r.json())

r = requests.post(f'{base_url}/find_drivers_who_have_been_in_position', data={'year': '2014'})
print(r.json())

r = requests.post(f'{base_url}/find_countries_wins', data={'position': '1'})
print(r.json())



r = requests.post(f'{base_url}/average_pitstop_of_drivers', data={'race_id' : 1002})
print(r.json())


r = requests.post(f'{base_url}/average_position_of_drivers_ascend', data={'race_year' : 2001})
print(r.json())


r = requests.post(f'{base_url}/the_drivers_for_their_nationality')
print(r.json())



