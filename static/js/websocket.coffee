wsUri = 'ws://127.0.0.1:8888/websocket'

init = ->
  feeder = document.getElementById('jsondiv')
  countid = 0
  testWebSocket()
  return

testWebSocket = ->
  websocket = new WebSocket(wsUri)

  websocket.onopen = (evt) ->
    onOpen evt
    return

  websocket.onclose = (evt) ->
    onClose evt
    return

  websocket.onmessage = (evt) ->
    onMessage evt
    return

  websocket.onerror = (evt) ->
    onError evt
    return

  return

onOpen = (evt) ->
  log_entry = 'Connected'
  console.log log_entry
  return

onClose = (evt) ->
  log_entry = 'Disconnected'
  console.log log_entry
  return

onMessage = (evt) ->
  #jdata = JSON.parse(evt.data)
  #text = jdata["text"]
  text = evt.data
  # html = "<h2>" + text  + "</h2>"
  html = text + '<br>'
  writeToFeed html
  countid += 1
  return

onError = (evt) ->
  log_entry = 'Error'
  console.log log_entry
  return

doSend = (message) ->
  websocket.send message
  return

writeToFeed = (message) ->
  feeder.innerHTML = message + feeder.innerHTML
  return

window.addEventListener 'load', init, false
