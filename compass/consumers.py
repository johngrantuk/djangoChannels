from channels import Group

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    print("Received!!")
    print(message)
    message.reply_channel.send({
        "text": "WS MEssage mother fucjer",
    })
    
def ws_connect(message):
    print("Someone connected.")
    message.reply_channel.send({
        "text": "Well thanks for reaching out - we're connected!",
    })