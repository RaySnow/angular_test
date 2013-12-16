import tornado.httpserver
import tornado.ioloop
from src.server import application

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8008)
    tornado.ioloop.IOLoop.instance().start()

