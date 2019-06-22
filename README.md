# Teams IXC Booking Bot
A bot that helps in the booking process for Cisco's IXC @ Dubai.
Submission for the Cisco EMEA

Libraries used in this project :

  - webexteamsbot : https://pypi.org/project/webexteamsbot/
  - Some Python standard libraries (requests, os, configparser)
  
  
# How do I run this bot on my machine ?
  
  - Download the IXC Booking Bot.py from this repo
  
  - Install the previously referenced library in your folder (webexteamsbot)
  
  - Create another .py file for your environment variables (Booked API session token, Cisco Teams API token...), you can name 
    it environmentVariables.py if you don't want to make any changes on the main Bot code.
    Check Annex 2 if you don't know how to set your environment variables.
    
  - In case you're not deploying the bot online and want to test it on your localhost, you need to make your localhost
    available to the internet (i.e exposing your bot to the internet). I used ngrok as a tunneling technology.
    Obviously you can use your own choice (localTunnel or serveo are good alternatives).
    Here is a Cisco Devnet tutorial on how to use ngrok : 
    https://developer.cisco.com/learning/lab/collab-spark-botl-ngrok/step/1
    
  - That's it ! Now go and run your Bot/Flask server and test the bot :)
  
  
# Annexes
  Annexe 1 : what are the commands accepted by the bot ?

        /echo: Reply back with the same message sent.
        /help: Get help.
        /hi: I say Hi
        /reservations: I show you the IXC reservations
        /title: Start your IXC reservation with a title
        /start: Please enter start date
        /end: Please enter the end date of your booking
        /sfdc: Please the SFDC deal ID
        /create: Will create a reservation based on your input
        
     
  Annexe 2 : environmentVariables.py content ?
  
   import os 

   -- Set environment variables

   os.environ['bot_email'] = 'YOUR BOT EMAIL, or you can use the already created one : '
   os.environ['teams_token'] = 'YOUR TOKEN'
   os.environ['bot_url'] = 'YOUR BOT URL'
   os.environ['bot_app_name'] = 'IXCBooking'
   os.environ['uid'] = 'YOUR BOOKED API UID'
   os.environ['session_token'] = 'YOUR SESSION TOKEN'
   os.environ['url_schedule'] = 'Get this URL from IXC admins :)'
   os.environ['url_create'] = 'Get this URL from IXC admins :) '





  -- Retrieve set environment variables
  bot_email = os.environ.get('bot_email')
  teams_token = os.environ.get('teams_token')
  bot_url = os.environ.get('bot_url')
  bot_app_name = os.environ.get('bot_app_name')
  uid = os.environ.get('uid')
  session_token=os.environ.get('session_token')
  url_schedule=os.environ.get('url_schedule')
  url_create=os.environ.get('url_create')



  
That's it ! 
Thanks for sticking around :)

Created by Farid EL HAJIM

Credits :

Cisco IXC Dubai team.
CSAP Prague team.
Cisco Software PoV team.
Cisco SE programmability makers community.
