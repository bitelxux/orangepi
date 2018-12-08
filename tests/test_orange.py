#!/usr/bin/python

import mock
import os
import sys
import unittest
from mock import MagicMock
from mock import patch

current = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current + '/../')
sys.path.insert(0, current + './pyA20')

flask = MagicMock()
class Flask(object):
    def __init__(*args, **kw):
        pass

    @staticmethod
    def route(debug=False):
        def _route(func):
            def inner(*args, **kwargs):
                func(*args, **kwargs)
            return inner
        return _route

flask.Flask = Flask

sys.modules['flask'] = flask

import server

class TestOrange(unittest.TestCase):

    def setUp(self):
        pass


    def test_01(self):
        pass
