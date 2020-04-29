import json

from connexion import NoContent
from cterasdk.exception import CTERAClientException

from ctera_gateway_openapi.managers.base_manager import BaseManager


class UsersManager(BaseManager):
    def get(self, name):
        try:
            user = self._gateway.users.get(name=name)
        except CTERAClientException as e:
            response = getattr(e, 'response')
            if response is not None:
                return NoContent, response.code
        return json.loads(str(user))

    def list_users(self):
        return [json.loads(str(user)) for user in self._gateway.users.get()]

    def add_user(self, name, password, full_name, email, uid):
        self._gateway.users.add(name, password, full_name=full_name, email=email, uid=uid)
        return NoContent, 201

    def modify_user(self, name, password=None, full_name=None, email=None, uid=None):
        self._gateway.users.modify(name, password=password, full_name=full_name, email=email, uid=uid)
        return NoContent, 201

    def delete(self, name):
        self._gateway.users.delete(name)
        return NoContent, 201
