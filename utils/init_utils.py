from flask_restful import Api, Resource
from url_list import URL_LIST
from importlib import import_module

def create_restful_api(app):
    api = Api(app)
    for url_obj in URL_LIST:
        print("\n#####", url_obj.resource,"\n")
        resource_name = url_obj.resource
        rsplit = resource_name.split(".")
        print("\n#####",rsplit,"\n")
        module, resource = ".".join(rsplit[:-1]), rsplit[-1]
        print("\n#####",module,resource,"\n")
        imported_module = getattr(import_module(module), resource)
        print("\n######",imported_module,"\n")
        api.add_resource(imported_module, url_obj.url, endpoint=url_obj.name)
