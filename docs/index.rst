Flask-BasicAuth
===============

Flask-BasicAuth is a Flask extension that provides an easy way to protect
certain views or your whole application with HTTP `basic access
authentication`_.

.. _basic access authentication: http://en.wikipedia.org/wiki/Basic_access_authentication


Installation
------------

The easiest way to install Flask-BasicAuth is with pip::

    pip install Flask-BasicAuth


Usage
-----

Usage of Flask-BasicAuth is simple::

    from flask import Flask, render_template
    from flask.ext.basic_auth import BasicAuth

    app = Flask(__name__)

    app.config['BASIC_AUTH_USERNAME'] = 'john'
    app.config['BASIC_AUTH_PASSWORD'] = 'matrix'

    basic_auth = BasicAuth(app)

    @app.route('/secret')
    @basic_auth.required
    def secret_view():
        return render_template('secret.html')

If you would like to protect you entire site with basic access authentication,
just set ``BASIC_AUTH_FORCE`` configuration variable to `True`::

    app.config['BASIC_AUTH_FORCE'] = True

You might find this useful, for example, if you would like to protect your
staging server from uninvited guests.

.. warning::

   Please make sure that you use SSL/TLS (HTTPS) to encrypt the connection
   between the client and the server, when using basic access authentication.
   In basic access authentication username and password are sent in cleartext,
   and if SSL/TLS is not used, the credentials could be easily intercepted.


Configuration
-------------

The following configuration values exist for Flask-BasicAuth.  Flask-BasicAuth
loads these values from your main Flask config which can be populated in
various ways.

A list of configuration keys currently understood by the extension:

``BASIC_AUTH_FORCE``
    If set to `True`, makes the whole site require HTTP basic access
    authentication.

    Defaults to `False`.

``BASIC_AUTH_REALM``
    The authentication realm used for the challenge. This is typically a
    description of the system being accessed.

    Defaults to ``''``.

``BASIC_AUTH_USERNAME`` and ``BASIC_AUTH_PASSWORD``
    The correct username and password combination that grants access for the
    client to the protected resource.

    You can override :meth:`BasicAuth.check_credentials <flask.ext.basicauth.BasicAuth.check_credentials>`,
    if you need a different authentication logic for your application.


API reference
-------------

.. module:: flask.ext.basicauth

This part of the documentation covers all the public classes and functions
in Flask-BasicAuth.

.. autoclass:: BasicAuth
   :members:


.. include:: ../CHANGES.rst


License
-------

.. include:: ../LICENSE
