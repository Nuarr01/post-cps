import requests
import random
import time
import os
from colorama import Fore

channel_id = input("Masukkan ID channel: ")
min_waktu = int(input("Set Waktu Minimum Kirim Pesan (detik): "))
max_waktu = int(input("Set Waktu Maksimum Kirim Pesan (detik): "))

time.sleep(1)
print("Script Kan Segera Di Mulai")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
    channel_id = channel_id.strip()

    payload = {
        'content': ''.join(words).strip()
    }

    headers = {
        'Authorization': authorization
    }

    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Sent message: ")
    print(Fore.YELLOW + payload['content'])

    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

    if response.status_code == 200:
        messages = response.json()
        if len(messages) == 0:
            is_running = False
            break
        else:
            # Generate random time interval
            waktu = random.randint(min_waktu, max_waktu)
            time.sleep(waktu)
