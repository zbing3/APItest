import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """docstring for BaseHandler"""
    def get_current_user(self):
        user_data = self.get_secure_cookie("user")
        if not user_data: return None
        return user_data
