import os
from slackclient import SlackClient
#BOT ID IS U5Y5BTPU2
BOT_NAME = 'goodmorningvietnam'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
if __name__ == "__main__":

    api_call = slack_client.api_call("users.list")
    if(api_call).get('ok'):
        #retireve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print ("Bot ID fir '" + user['name'] + "' is " + user.get('id'))
                #going to just continue.
