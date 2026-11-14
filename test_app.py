"""Tests for app.py. Run: python -m unittest -v"""
import threading
import unittest
import urllib.request

import app


class GreetingTest(unittest.TestCase):
    """Unit tests: the greeting() function."""

    def test_default_greeting_contains_student(self):
        self.assertEqual(app.greeting(), "Hello from Jenkins pipeline, Mykytyshyn!")

    def test_greeting_with_custom_name(self):
        self.assertIn("Jenkins", app.greeting("Jenkins"))


class HttpTest(unittest.TestCase):
    """Integration test: start the server and send a real HTTP request."""

    def setUp(self):
        self.server = app.make_server(port=0)          # port 0 = any free port
        self.port = self.server.server_address[1]
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def test_http_response(self):
        with urllib.request.urlopen(f"http://127.0.0.1:{self.port}/") as resp:
            self.assertEqual(resp.status, 200)
            self.assertEqual(resp.read().decode("utf-8").strip(), app.greeting())


if __name__ == "__main__":
    unittest.main()
