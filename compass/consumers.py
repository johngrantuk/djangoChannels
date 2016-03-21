from channels import Group
from channels.sessions import channel_session

@channel_session
def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    print("Received!!")
    worker = message.channel_session['worker']                                  # Checks where message came from.
    
    if worker == 'compass':
        Group('compass').send({'text': message['text']})
    else:
        message.reply_channel.send({
           "text": "I don't know what worker you are... :(",
        })

 
@channel_session   
def ws_connect(message):
    print("Someone connected.")
    path = message['path']                      # i.e. /compass/
    print(str(type(path)))
    print("Path = " + str(path))
    
    if path == b'/compass/':
        print("Adding new user to compass group")
        message.channel_session['worker'] = "compass"                           # Allows for persistance
        Group("compass").add(message.reply_channel)                             # Adds user to group for broadcast
        message.reply_channel.send({
           "text": "You're connected to compass :) ",
        })
    else:
        print("Strange connector!!")
    
@channel_session
def ws_disconnect(message):
    print("Someone left us...")
    worker = message.channel_session['worker']                                  # Checks where message came from.
    
    if worker == 'compass':
        print("Compass down.")
        Group('compass').discard(message.reply_channel)
    else:
        print("I don't know who it was though.")
    