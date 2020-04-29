import logging

import connexion
from connexion.resolver import RestyResolver

from ctera_gateway_openapi.common.config import Config


logging.basicConfig(level=logging.DEBUG)
Config.instance()

app = connexion.FlaskApp(__name__)
app.add_api('api.yml', resolver=RestyResolver('ctera_gateway_openapi.api'))
application = app.app # expose global WSGI application object
