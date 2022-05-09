const socket = new WebSocket("wss://javascript.info/article/websocket/demo/hello");

// Example code for sockets
socket.onopen = function(e) {
	console.log("[open] Connection established");
	console.log("Sending to server");
	socket.send("My name is John");
};

socket.onmessage = (event) => {
	console.log(`[message] Data received from server: ${event.data}`);
};

socket.onclose = function(event) {
	if (event.wasClean) {
		console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
	} else {
		// e.g. server process killed or network down
		// event.code is usually 1006 in this case
		console.log('[close] Connection died');
	}
};

socket.onerror = function(error) {
	console.error(`[error] ${error.message}`);
};
