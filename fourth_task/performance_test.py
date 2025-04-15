import requests
import time

base_url = 'http://127.0.0.1:5000'

start = time.time()
user_response = requests.get(f'{base_url}/user/1')
if user_response.status_code == 200:
    user_id = '1'
    details_response = requests.get(f'{base_url}/user/{user_id}/details')
    print("Details:", details_response.json())
else:
    print("User not found")
end = time.time()
print(f"Complex scenario test took {end - start:.2f} seconds")