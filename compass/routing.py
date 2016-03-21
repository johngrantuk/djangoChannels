from compass.consumers import ws_message, ws_connect

channel_routing = {
    'websocket.connect': ws_connect,
    "websocket.receive": ws_message,
}