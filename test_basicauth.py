from __future__ import with_statement

import base64
import unittest

from flask import Flask
from flask.ext.basicauth import BasicAuth


class BasicAuthTestCase(unittest.TestCase):

    def assertIn(self, value, container):
        self.assertTrue(value in container)

    def setUp(self):
        app = Flask(__name__)

        app.config['BASIC_AUTH_USERNAME'] = 'john'
        app.config['BASIC_AUTH_PASSWORD'] = 'matrix'

        basic_auth = BasicAuth(app)

        @app.route('/')
        def normal_view():
            return 'This view does not normally require authentication.'

        @app.route('/protected')
        @basic_auth.required
        def protected_view():
            return 'This view always requires authentication.'

        self.app = app
        self.basic_auth = basic_auth
        self.client = app.test_client()

    def test_sets_default_values_for_configuration(self):
        self.assertEqual(self.app.config['BASIC_AUTH_REALM'], '')
        self.assertEqual(self.app.config['BASIC_AUTH_FORCE'], False)

    def test_views_without_basic_auth_decorator_respond_with_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_requires_authentication_for_all_views_when_forced(self):
        self.app.config['BASIC_AUTH_FORCE'] = True
        response = self.client.get('/')
        self.assertEqual(response.status_code, 401)

    def test_responds_with_401_without_authorization(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)

    def test_asks_for_authentication(self):
        response = self.client.get('/protected')
        self.assertIn('WWW-Authenticate', response.headers)
        self.assertEqual(
            response.headers['WWW-Authenticate'],
            'Basic realm=""'
        )

    def test_asks_for_authentication_with_custom_realm(self):
        self.app.config['BASIC_AUTH_REALM'] = 'Secure Area'
        response = self.client.get('/protected')
        self.assertIn('WWW-Authenticate', response.headers)
        self.assertEqual(
            response.headers['WWW-Authenticate'],
            'Basic realm="Secure Area"'
        )

    def test_check_credentials_with_correct_credentials(self):
        with self.app.test_request_context():
            self.assertTrue(
                self.basic_auth.check_credentials('john', 'matrix')
            )

    def test_check_credentials_with_incorrect_credentials(self):
        with self.app.test_request_context():
            self.assertFalse(
                self.basic_auth.check_credentials('john', 'rambo')
            )

    def test_responds_with_401_with_incorrect_credentials(self):
        auth = base64.encodestring("john:rambo").strip('\r\n')
        response = self.client.get('/protected',
            headers={'Authorization': 'Basic ' + auth})
        self.assertEqual(response.status_code, 401)

    def test_responds_with_200_with_correct_credentials(self):
        auth = base64.encodestring("john:matrix").strip('\r\n')
        response = self.client.get('/protected',
            headers={'Authorization': 'Basic ' + auth})
        self.assertEqual(response.status_code, 200)

    def test_runs_decorated_view_after_authentication(self):
        auth = base64.encodestring("john:matrix").strip('\r\n')
        response = self.client.get('/protected',
            headers={'Authorization': 'Basic ' + auth})
        self.assertEqual(
            response.data,
            'This view always requires authentication.'
        )


def suite():
    return unittest.makeSuite(BasicAuthTestCase)


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
