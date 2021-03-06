import unittest
from collections import namedtuple
import json
from paypalrestsdk.exceptions import *

class TestExceptions(unittest.TestCase):

  def setUp(self):
    self.Response = namedtuple('Response', 'status_code reason')

  def test_connection(self):
    error = ConnectionError({})
    self.assertEqual(str(error), "Failed.")

  def test_redirect(self):
    error = Redirection({ "Location": "http://example.com" })
    self.assertEqual(str(error), "Failed. => http://example.com")

  def test_not_found(self):
    response = self.Response(status_code="404", reason="Not Found" )
    error = ResourceNotFound(response)
    self.assertEqual(str(error), "Failed. Response status: %s. Response message: %s." % (response.status_code, response.reason))

  def test_unauthorized_access(self):
    response = self.Response(status_code="401", reason="Unauthorized" )
    error = UnauthorizedAccess(response)
    self.assertEqual(str(error), "Failed. Response status: %s. Response message: %s." % (response.status_code, response.reason))

  def test_missing_param(self):
    error = MissingParam("Missing Payment Id")
    self.assertEqual(str(error), "Missing Payment Id")

  def test_missing_config(self):
    error = MissingParam("Missing client_id")
    self.assertEqual(str(error), "Missing client_id")

