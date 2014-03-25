#coding=utf-8
import os
import tornado.ioloop
import tornado.web
import tornado.httpserver

from tornado.options import define, options
from handlers import web



define("port", default=5210, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", web.view),
            (r"/_get_api", web.get_api)
            # (r"/auth/login", auth.LoginHandler),
            # (r"/auth/logout", auth.LogoutHandler),
            ]       
        settings = dict(
                cookie_secret="cetenas*&3408147@!$^)*d",
                login_url="/auth/login",
                debug = True,
                static_path = os.path.join(os.path.dirname(__file__), "static"),
                template_path = os.path.join(os.path.dirname(__file__), "templates")
            )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    main()
