class URL(object):
    def __init__(self, url, resource, name=None):
        self.url = url
        self.resource = resource
        self.name = name

URL_LIST = [
    URL("/users", "resources.users.Users", name="users")
]
