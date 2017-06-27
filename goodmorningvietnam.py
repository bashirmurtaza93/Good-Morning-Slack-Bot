import os
import time
import datetime
from slackclient import SlackClient

#Good morning vietnam's ID is inside of a enviorment variable

BOT_ID = os.environ.get("BOT_ID")
print(BOT_ID)

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

#instantiate Slack and something
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
print(dir(slack_client))

def handle_command(username,channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Hey "+username+ " ....ahhhhh Goooooood Morning Vietnam!!!!!"
    slack_client.api_call("chat.postMessage", channel=channel, text=response, attachments='[{"title":"test","image_url":"https://media.giphy.com/media/BYG86QlGgaHvy/giphy.gif"}]', as_user=True)

def findUser(user_list, user_id):
    users = user_list.get('members')
    for user in users:
        if user.get('id') == user_id:
            return user.get('name')


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output

    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                user_id = output['user'];
                user_list = slack_client.api_call('users.list')
                username = findUser(user_list,user_id)
                return username, output['channel']
    return None, None


def goodMorningEveryone():
    user_list = slack_client.api_call('users.list').get('members')
    username_list = []
    for user in user_list:
        if user.get('name') != 'goodmorningvietnam':
            username_list.append(user.get('name'))

    channel_list = slack_client.api_call('channels.list').get('channels')
    for channel in channel_list:
        if channel.get('name') == 'general':
            general_channel_id = channel.get('id')
    str_username_list = ', '.join(username_list)
    response = 'Hello ' + str_username_list + ' and ....'
    slack_client.api_call("chat.postMessage", channel=general_channel_id, text=response, attachments='[{"title":"test","image_url":"https://media.giphy.com/media/BYG86QlGgaHvy/giphy.gif"}]', as_user=True)




if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("goodmorningvietnam connected and running")
        if time.strftime("%H:%M") == '14:00':
            goodMorningEveryone()
        # print(time.strftime("%H:%M"))
        while True:

            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command,channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid slack token or bot id")
