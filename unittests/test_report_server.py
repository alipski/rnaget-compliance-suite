# -*- coding: utf-8 -*-
"""Module unittests.test_report_server.py

This module contains methods to test the report_server module via pytest.
"""

import os
import time
import signal
from multiprocessing import Process
from compliance_suite.report_server import capitalize, ReportServer

def spawn_report_server():
    """spawn a sample report server as a subprocess"""
    rs = ReportServer()
    rs.set_free_port()
    rs.serve_thread()

def test_capitalize():
    """asserts capitalize function works as expected"""

    word = "word"
    assert capitalize(word) == "Word"

def test_keyboard_interrupt():
    """asserts keyboard interrupts are caught and lead to program shutdown"""

    # start a server, send a keyboard interrupt to the process, then check
    # that the process is no longer alive and exited without error (code 0)
    p = Process(target=spawn_report_server)
    p.start()
    time.sleep(2)
    os.kill(p.pid, signal.SIGINT)
    time.sleep(2)
    assert p.is_alive() == False
    assert p.exitcode == 0
