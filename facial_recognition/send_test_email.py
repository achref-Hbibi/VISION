#! /usr/bin/python

# Imports
import requests

def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandbox66e9387ceb5a4e10a127aa1d6263e548.mailgun.org/messages",
        auth=("api", "55b5fe432788943c16e6314bd5803195-fe066263-85b24cd9"),
        data={"from": 'hello@example.com',
              "to": ["achrefhbibi.issat@gmail.com"],
            "subject": "Visitor Alert",
            "html": "<html> Your Raspberry Pi recognizes someone. </html>"})
                      
request = send_simple_message()
print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))
