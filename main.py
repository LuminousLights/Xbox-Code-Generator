import requests
import time
import random, string
from discord import Webhook, RequestsWebhookAdapter
import colorama
from colorama import Fore, Back, Style
import os
colorama.init()
# Copyright (c) 2022 skyblue#8900
# Using this tool you use it for educational purposes
# If misuse, i am not responsible for any damages that has happend

print(f'''{Fore.RED}
Loading.. Xbox Code Generator ~coded by fluro#0009~
''')
time.sleep(1.5)
os.system('cls')

print(f'''{Fore.RED}
      
$$\   $$\ $$\                                  $$$$$$\                  $$\           
$$ |  $$ |$$ |                                $$  __$$\                 $$ |          
\$$\ $$  |$$$$$$$\   $$$$$$\  $$\   $$\       $$ /  \__| $$$$$$\   $$$$$$$ | $$$$$$\  
 \$$$$  / $$  __$$\ $$  __$$\ \$$\ $$  |      $$ |      $$  __$$\ $$  __$$ |$$  __$$\ 
 $$  $$<  $$ |  $$ |$$ /  $$ | \$$$$  /       $$ |      $$ /  $$ |$$ /  $$ |$$$$$$$$ |
$$  /\$$\ $$ |  $$ |$$ |  $$ | $$  $$<        $$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|
$$ /  $$ |$$$$$$$  |\$$$$$$  |$$  /\$$\       \$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$\ 
\__|  \__|\_______/  \______/ \__/  \__|       \______/  \______/  \_______| \_______|
                                                                                      
''')

time.sleep(1.5)
print("Credit to skyblue#8900")
time.sleep(0.5)
print("Or Luminou")
time.sleep(0.5)
print("Note to stop generating click ctrl and c")
time.sleep(1.5)
link = input("Webhook link :")
amount = int(input("How many Xbox codes :"))
for i in range(amount):
    time.sleep(0.3)
    code = "AB" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "CD" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "EF" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "FG" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "GH" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "HI" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "JK" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "LM" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "NO" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "PQ" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "RS" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "TU" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "VX" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "WY" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "ZA" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "CY" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "CB" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "AA" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "BB" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "BY" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "BC" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "CY" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "CC" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "DY" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "DD" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    code = "EY" + "".join(random.choices(string.ascii_letters + string.digits, k=23))
    print("[GENERATED CODE] " + code)
    webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
    webhook.send(code)