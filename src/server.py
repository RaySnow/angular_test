# coding:utf-8
from datetime import datetime
import json
import tornado
from tornado import web, template
import os

from jinja2 import Environment, FileSystemLoader

from models import connection

templates_folder_path = os.path.join(os.path.dirname(__file__), 'templates')
static_folder_path = os.path.join(os.path.dirname(__file__), 'static')

env = Environment(loader=FileSystemLoader(templates_folder_path), variable_start_string="{*",
                  variable_end_string="*}")


class Jinja2TemplateLoader(template.Loader):
    def _create_template(self, name):
        template = env.get_template(name)
        template.generate = template.render
        return template


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("index.html")


class ClientHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_argument('email', default=False, strip=True)
        mobile = self.get_argument('mobile', default=False, strip=True)
        if email:
            user = connection.User()
            user.email = email
            user.mobile = u''
            user.created_at = datetime.now()
            user.save()
            self.finish({'status': 'ok'})
        if mobile:
            user = connection.User()
            user.mobile = mobile
            user.email = u''
            user.created_at = datetime.now()
            user.save()
            self.finish({'status': 'ok'})
        else:
            self.finish({'status': 'error'})


handlers = [(r"/", MainHandler),
            (r"/info", ClientHandler)]
settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    cookie_secret="__TODO:_HAO_PING_JIA_SECRET__",
    template_loader=Jinja2TemplateLoader(templates_folder_path),
    debug=True
)
my_client = None
application = tornado.web.Application(handlers, **settings)


