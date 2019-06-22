import os
import requests
import environmentVariables
from webexteamsbot import TeamsBot
from requests.auth import HTTPBasicAuth
import sys
import configparser

# Bypass some urllib3 warnings
try:
    requests.packages.urllib3.disable_warnings() 
except: 
    pass 

# Setting up Environment variables from external module

bot_email = environmentVariables.bot_email
teams_token = environmentVariables.teams_token
bot_url = environmentVariables.bot_url
bot_app_name = environmentVariables.bot_app_name
uid = environmentVariables.uid
session_token = environmentVariables.session_token
url_schedule=environmentVariables.url_schedule
url_create=environmentVariables.url_create
title = ""
sDate = ""
eDate = ""
sfdc = ""

# Create a Bot Object
bot = TeamsBot(

    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
)


# Sample greeting function to test the bot

def greeting(incoming_msg):
    
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = "Hello {}, I'm a chat bot. ".format(sender.firstName)
    response += "See what I can do by asking for **/help**."
    global title
    print ("from hi :" + title)
    return response


# Getting reservations details from Booked API, unfortunately the API doesn't give accurate reservation info.

def get_reservations(incoming_msg):

    global session_token
    global uid
    global url_schedule

    url = url_schedule

    payload = ""
    headers = {
        'X-Booked-SessionToken': session_token,
        'X-Booked-UserId': uid,
        'cache-control': "no-cache",
        }

    response = requests.request("GET", url, data=payload, headers=headers, verify=False)

    print(response.text)
    json_response=response.json()
    reservation=json_response['periods'][0][0]
    reservation2=str(reservation)
    return reservation2



# Start of reservation information gathering from the user

    # Function to get the title

def giveTitle(incoming_msg):

    config = configparser.ConfigParser()
    config['attributes'] = {}
    config['attributes']['Title'] = incoming_msg.text[7:]
    with open(incoming_msg.personId, 'w') as configfile:
        config.write(configfile)

    return " Title saved, please enter your prefered Start date in the right format (07/25/201914:00:00) using the /start command; example : /start 07/25/201914:00:00"

    # Function to get the start date
def startDate(incoming_msg):

    config = configparser.ConfigParser()
    config['attributes1'] = {}
    config['attributes1']['Start Date'] = incoming_msg.text[7:]
    with open(incoming_msg.personId, 'a') as configfile:
        config.write(configfile)

    return "Start date saved, please enter End date in the right format (07/25/201915:00:00) using the /end command; example : /end 07/25/201915:00:00"


    # Function to get the end date
def endDate(incoming_msg):

    config = configparser.ConfigParser()
    config['attributes2'] = {}
    config['attributes2']['End Date'] = incoming_msg.text[5:]
    with open(incoming_msg.personId, 'a') as configfile:
        config.write(configfile)
    return "End date saved, please enter a valid Salesforce deal ID with /sfdc command; example : /sfdc 123456"

    # Function to get the SFDC deal ID

def sfdc(incoming_msg):
    config = configparser.ConfigParser()
    config['attributes3'] = {}
    config['attributes3']['sfdc'] = incoming_msg.text[6:]
    with open(incoming_msg.personId, 'a') as configfile:
        config.write(configfile)
    return "SFDC ID saved, please create your reservation with the /create command "

    # Just to test the file read/write thingy :)

def r(incoming_msg):
    config = configparser.ConfigParser()
    config.read(incoming_msg.personId)   
    print(config['attributes']['title'])
    return incoming_msg.personId


    # Create the reservation with the saved info

def create_reservation(incoming_msg):
  
    import requests
    import json

    global url_create
    global uid
    global session_token


    url = url_create

    config = configparser.ConfigParser()
    config.read(incoming_msg.personId)   

    payload = { 
        
        "description": "Reservation",
        "endDateTime": config['attributes2']['End Date'],
        "participants": "",
        "participatingGuests": [
            "felhajim@cisco.com"
        ],
        "invitedGuests": "",
        "recurrenceRule": "",
        "resourceId": 9,
        "resources": "",
        "startDateTime": config['attributes1']['Start Date'],
        "title": config['attributes']['Title'],
        "userId": uid,
        "customAttributes":[{"attributeId":"12","attributeValue": str(config['attributes3']['sfdc'])}],
        "startReminder": "",
        "endReminder": "",
        "allowParticipation": True,
        "retryParameters": "",
        "termsAccepted": True

}
    print (payload)

    headers = {
    'Content-Type': "application/json",
    'X-Booked-SessionToken': session_token,
    'X-Booked-UserId': uid,
    'cache-control': "no-cache",

    }

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)

    return "Reservation created ! You'll receive a confirmation mail shortly, now please fill in the briefing document by following this link : http://ixc.cisco.com/ixc/form/ixc-briefing , see you @ IXC ! :) "
 

# Bot commands :)

bot.add_command("/hi", "I say Hi", greeting)
bot.add_command("/reservations", 'Shows IXC reservation (Not implemented)', get_reservations)
bot.add_command("/title", 'Start your IXC reservation with a title', giveTitle)
bot.add_command("/start", 'After entering the title, enter a start date please for your booking', startDate)
bot.add_command("/end", 'After entering the start date, enter a end date please for your booking', endDate)
bot.add_command("/sfdc", 'After entering a start and end date, please enter a VALID sfdc deal ID', sfdc)
bot.add_command("/create", 'Will create a reservation based on your input', create_reservation)


if __name__ == "__main__":
    # Run Bots
    bot.run(host="127.0.0.1", port=8080)



