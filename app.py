import os
import time
import tornado.ioloop
import tornado.web
import tornado.template
import tornado.httpserver
import tornado.websocket


#App Routes
class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")



#JSON Handlers
class JSONHandler(tornado.web.RequestHandler):
  def get(self):
    self.write({"test" : "some test JSON"})





#WebSocket Handlers
class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
      print "WebSocket opened"
      counter = 1
      while counter < 10:
        self.write_message({"counter" : counter})
        counter += 1

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print "WebSocket closed"



settings = {
  "static_path": os.path.join(os.path.dirname(__file__), "static"),
  "template_path": os.path.join(os.path.dirname(__file__), "templates"),
  }



application = tornado.web.Application([
  (r"/", MainHandler),
  (r"/json", JSONHandler),
  (r"/websocket", EchoWebSocket),
  ], **settings)



if __name__ == "__main__":
  server = tornado.httpserver.HTTPServer(application)
  server.bind(8888)
  server.start(0)  # Forks multiple sub-processes
  tornado.ioloop.IOLoop.instance().start()
