import requests
import time
import sys
import subprocess
import re
import webbrowser
for i in range (10):
    print("Booting: sendtowebhook.py" + "." * i, end="\r")
    time.sleep(0.5)
print("#############################")
time.sleep(0.3)
print("##### WEBHOOK REQUESTER #####")
time.sleep(0.3)
print("#############################")
time.sleep(0.3)
print("")
print("Sends a request to a webhook URL with customizable data")
print("")
time.sleep(0.3)
webhook = input("Webhook URL: ")
print("Accepted!")
data = input("Data to be sent: ")
for i in range(10):
    print("Setting up request connection" + "." * i, end="\r")
    time.sleep(0.5)
print("")
print("")
ready = input("Send?(y/n): ")
if ready == "n":
    print("ABORTED")
    sys.exit()
elif ready == "y":
    response = requests.post(webhook, json=data)
    if response.status_code == 200:
        print("Sent!")
    else:
        print("Error sending data to webhook.")

