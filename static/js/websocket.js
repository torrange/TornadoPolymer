var wsUri = "ws://127.0.0.1:8888/websocket";

function init()
{
  feeder = document.getElementById("jsondiv")
  countid = 0
  testWebSocket();
}

function testWebSocket()
{
  websocket = new WebSocket(wsUri);
  websocket.onopen = function(evt) { onOpen(evt) };
  websocket.onclose = function(evt) { onClose(evt) };
  websocket.onmessage = function(evt) { onMessage(evt) };
  websocket.onerror = function(evt) { onError(evt) };
}

function onOpen(evt)
{
  var log_entry = "Connected"
  console.log(log_entry)
}

function onClose(evt)
{
  var log_entry = "Disconnected"
  console.log(log_entry)
}

function onMessage(evt)
{
  //jdata = JSON.parse(evt.data)
  //text = jdata["text"]
  text = evt.data
  // html = "<h2>" + text  + "</h2>"
  html = text+"<br>"
  writeToFeed(html);
  countid += 1
}

function onError(evt)
{
  var log_entry = "Error"
  console.log(log_entry)
}

function doSend(message)
{ 
  websocket.send(message);
}

function writeToFeed(message)
{
  feeder.innerHTML = message + feeder.innerHTML;
}

window.addEventListener("load", init, false);