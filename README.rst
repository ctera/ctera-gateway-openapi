*****************************************
OpenAPI compatible server for CTERA Filer
*****************************************
Implementation of an OpenAPI compatible server for CTERA Filer

Documentation
#############
To be Added

Installation
############
Currently you can only run from the code

.. code-block:: console

   $ git clone https://github.com/ctera/ctera-gateway-openapi.git
   $ cd ctera-python-sdk

Running in a VirtualEnv
#######################
Create a Virtual Environment and install requirements
*****************************************************

.. code-block:: console

   $ virtualenv --python=/usr/bin/python3 venv
   $ source venv/bin/activate
   $ pip install -r requirements.txt

Run the server
**************

.. code-block:: console

   $ source venv/bin/activate
   $ CTERA_FILER_ADDRESS=<IP or FQND of the CTERA Filer> CTERA_FILER_USERNAME=<User name to use> CTERA_FILER_PASSWORD=<Password to use> uwsgi --yaml etc/uwsgi.yml --pidfile /tmp/uwsgi.pid

The server will run on port 9090. You may access the `SWAGGER UI <http://localhost:9090/v1.0/ui/>`_