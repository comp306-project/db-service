import requests


base_url = f'http://localhost:5000/'

r = requests.post(f'{base_url}/find_average_laptime_by_race_id_and_driver_id', data={'race_id' : 1009, 'driver_id' : 1})
print(r.json())
