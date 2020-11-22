from importlib import import_module
import unittest


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        flask_app = import_module('validate')
        flask_app.app.testing = True
        self.app = flask_app.app.test_client()

    def test_validate_ok(self):
        name = 'sato'
        actual = self.app.post('/validate', data=dict(name=name, name2=name), follow_redirects=True)
        assert actual.status_code == 200
        assert '入力チェック、問題なしです！' in actual.get_data(as_text=True)

    def test_validate_ng(self):
        name = 'sato'
        actual = self.app.post('/validate', data=dict(name=name, name2=''), follow_redirects=True)
        assert actual.status_code == 200
        assert '入力内容が一致しません' in actual.get_data(as_text=True)
