# -*- coding: utf-8 -*-
"""Module unittests.test_user_config_parser.py

This module contains methods to test the user_config_parser module via pytest.

Attributes:
    yaml_dir (str): path to dir containing sample user config files
    user_config_pass (str): yaml file that should pass config validation
    user_config_file_not_found (str): yaml file that does not exist, fail
"""

from compliance_suite.user_config_parser import UserConfigParser

yaml_dir = "unittests/testdata/user_config/"
user_config_pass = "user_config_template.yaml"
user_config_file_not_found = "file_not_found.yaml"

def test_constructor():
    """asserts attributes set correctly via constructor"""

    parser = UserConfigParser(user_config_pass)
    assert parser.config_file == user_config_pass
    assert parser.d == None

def test_parse_config_file_pass():
    """asserts yaml successfully loaded and contains expected values"""

    parser = UserConfigParser(user_config_pass)
    parser.parse_config_file()
    assert parser.d != None
    assert len(parser.d["servers"]) == 2

    server_a = parser.d["servers"][0]
    assert server_a["server_name"] == "Server A"
    assert server_a["base_url"] == "https://felcat.caltech.edu/rnaget/"

def test_parse_config_file_not_found():
    """asserts correct error raised when yaml file not found"""

    parser = None
    try:
        parser = UserConfigParser(user_config_file_not_found)
        parser.parse_config_file()
    except FileNotFoundError as e:
        assert str(e) == "user config file: " + user_config_file_not_found \
                         + " not found"

def test_validate_config_file_pass():
    """asserts correct yaml file passes validation"""

    parser = UserConfigParser(user_config_pass)
    parser.parse_config_file()
    parser.validate_config_file()

def test_validate_config_file_failures():
    """asserts parser invalidates different yaml files with message"""

    messages = [
        '"servers" should be the only root key',
        '"servers" should be the only root key',
        "missing attribute(s) from server 1: continuous, expressions, " 
            + "projects, studies",
        "missing attribute(s) from project 1 in Server A: filters, id",
        "YAML config file could not be parsed. Please refer to the template "
            + "config file.",
        'value of implemented:expressions must be a boolean',
        'wrongendpoint not a valid endpoint'
    ]

    for i in range(0,7):
        config_file = yaml_dir + "fail_" + str(i) + ".yaml"
        message = messages[i]

        try:
            parser = UserConfigParser(config_file)
            parser.parse_config_file()
            parser.validate_config_file()
        except Exception as e:
            assert message == str(e)

