from tinydb import TinyDB, Query
from tinydb.operations import delete
from tinydb_serialization import Serializer, SerializationMiddleware

from datetime import datetime

from nfvo_server.models.sfcr import SFCR
from nfvo_server.models.route import Route


class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime
    FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

    def encode(self, obj):
        return obj.strftime(self.FORMAT)

    def decode(self, s):
        # return datetime.strptime(s, self.FORMAT)
        # return raw string because from_dict() method require datetime in string format
        return s


serialization = SerializationMiddleware()
serialization.register_serializer(DateTimeSerializer(), 'TinyDate')

db = TinyDB('nfvo_server/database/db.json', storage=serialization)
routes = db.table('routes', cache_size=30)
active_requests = db.table('active_requests', cache_size=30)
query = Query()

def insert_route(route):
    routes.insert(route.to_dict())

def update_route(route):
    routes.upsert(route.to_dict(), query.id == route.id)

def update_active_request(active_request):
    active_requests.upsert(active_request.to_dict(), query.id == active_request.id)

def insert_active_request(active_request):
    active_requests.insert(active_request.to_dict())

def get_route(id):
    return Route.from_dict(routes.get(query.id == id))

def get_active_request(id):
    return SFCR.from_dict(active_requests.get(query.id == id))

def get_all_routes():
    return [Route.from_dict(route) for route in routes.all()]

def get_all_active_requests():
    return [SFCR.from_dict(sfcr) for sfcr in active_requests.all()]

def del_route(id):
    routes.remove(query.id == id)

def del_active_request(id):
    active_requests.remove(query.id == id)
