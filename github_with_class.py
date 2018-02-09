import urllib2 as rq

class Github(object):
    def __init__(self, username):
        self.username = username
        self.base_url = 'https://api.github.com/users/'
    def get_user_info(self):
        full_url = "{0}{1}".format(self.base_url, self.username)
        request = rq.Request(full_url)
        handler = rq.urlopen(request)
        if handler.getcode() == 200:
            return handler.read()
    def get_user_repos(self):
        full_url = "{0}{1}/repos".format(self.base_url, self.username)
        request = rq.Request(full_url)
        handler = rq.urlopen(request)
        if handler.getcode() == 200:
            return handler.read()

user = Github('tlcuzick')
print(user.get_user_info())
print(user.get_user_repos())

        