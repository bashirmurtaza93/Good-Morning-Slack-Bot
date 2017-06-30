#Good Morning Py Bot

A bot that will message you or your team good morning at a specific time you set it to.

###Getting Started

Download a copy of this build. Everything you will need to configure will be inside the goodmorning.py file.

### Prerequisites

You will need Python3 and PIP

### Getting everything up and running

Go create your own bot.

Once you get the access token for that bot. Hook it up and then get the BOT ID. You can get the BOT ID with the file print_bot_id.py

Once you've done that you can go into goodmorning.py

Go to the a specific comment that states where to set the time at the bottom

```
#***INSERT YOUR OWN TIME HERE***#
if time.strftime("%H:%M") == 'SET TIME HERE':
#Note this goes by 24 hour time.

```

From here you can set all the custom commands and attatchment files from here


```
#SET MESSAGES AND ATTTACHMENTS IN THE FOLLOWING 2 LINES#
response = 'Hello ' + str_username_list #This line by default says hello to your team.
slack_client.api_call("chat.postMessage", channel=general_channel_id, text=response, attachments='[{"title":"test","image_url":"Image URL goes here"}]', as_user=True)

```
You can also set what channel you want it to say good morning to by customizing the following field

```

if channel.get('name') == 'CHANNEL NAME HERE':
        general_channel_id = channel.get('id')

```
