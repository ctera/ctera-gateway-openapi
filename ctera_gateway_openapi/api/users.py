from connexion import NoContent

from ctera_gateway_openapi.managers.users import UsersManager


def get(userName):
    return UsersManager().get(userName)


def search():
    return UsersManager().list_users()


def post(body):
    password = body.get('password')
    if password is None:
        return NoContent, 400
    return UsersManager().add_user(body['username'], password, body.get('fullName'), body.get('email'), body.get('uid'))


def put(body):
    return UsersManager().add_user(body['username'], body.get('password'), body.get('fullName'), body.get('email'), body.get('uid'))


def delete(userName):
    return UsersManager().delete(userName)
