"""Test cases for app.py"""

from flask import Flask
from flask_testing import TestCase
from app import app


class TestApp(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config["TESTING"] = True
        return app

    def test_index(self):
        response = app.test_client().get("/")
        self.assert200(response)
        self.assert_template_used("base.html")

    def test_get_volume_no_parameters(self):
        response = app.test_client().get("/volume")
        self.assert_context("error_list", ["Input all fields"])
        self.assert400(response)
        self.assert_template_used("errors.html")

    def test_get_volume_incomplete_parameters(self):
        response = app.test_client().get("/volume?row=1&col=1")
        self.assert_context("error_list", ["Input all fields"])
        self.assert_template_used("errors.html")
        self.assert400(response)

    def test_get_volume_col_greater_than_row(self):
        response = app.test_client().get("/volume?row=1&col=2&liters=1.0")
        self.assert_context("error_list", ["row should be >= column"])
        self.assert_template_used("errors.html")
        self.assert400(response)

    def test_get_multiple_errors(self):
        response = app.test_client().get("/volume?row=1&col=2")
        self.assert_context("error_list", ["Input all fields", "row should be >= column"])
        self.assert_template_used("errors.html")
        self.assert400(response)

    def test_valid_input(self):
        response = app.test_client().get("/volume?row=1&col=1&liters=1.0")
        self.assert_template_used("results.html")
        self.assert_context("row", 1)
        self.assert_context("col", 1)
        self.assert_context("liters", 1)
        self.assert_context("result", 0.25)
        self.assert_context("glasses", [0.25, 0.25, 0.25])
        self.assert200(response)
