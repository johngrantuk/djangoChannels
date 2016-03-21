$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);
    
    chatsock.onopen = function() {
   		console.log("Connected!");
   		$('#heading').text("Connected!");
    	chatsock.send("Connected!");
	};
	
    chatsock.onmessage = function(message) {
    	console.log("Received Sock message!");
    	console.log(message);
    	$('#heading').text(message.data);
        //var data = JSON.parse(message.data);
    };
});