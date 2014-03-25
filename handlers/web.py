#coding=utf-8
import json
import requests
from handlers.base import BaseHandler


class view(BaseHandler):
    def get(self):
        return self.render("index.html")
class get_api(BaseHandler):
    def post(self):
        res = dict()
        args = self.request.arguments
        for a in args:
            res[a] = self.get_argument(a)
        url = res['url']
        method = res['method']
        data = eval(res['data'])
        headers = eval(res['headers'])
        # if data:
            # data = dict((d.split(':') for d in data.split(','))) 
        # if headers:
        #     headers = dict((h.split(':') for h in headers.split(',')))

        if method == "post":
            r = requests.post(url, data=json.dumps(data), headers=headers)
        if method == "get":
            r = requests.get(url, headers=headers, params=data)
        if method == "put":
            r = requests.put(url, data=json.dumps(data), headers=headers)
        if method == "delete":
            r = requests.delete(url, headers=headers)

        self.write(r.text)
            

