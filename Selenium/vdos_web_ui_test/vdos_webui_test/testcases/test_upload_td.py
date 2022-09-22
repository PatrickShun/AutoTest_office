#! /usr/bin/env python

import unittest

import utils as utils
from models.getconfig import Configure
from models.project import Project
import common as cons

config = Configure()

class TestUploadTd(unittest.TestCase):
    def setUp(self) -> None:
        utils.setup()

    def test_upload_correct_td_file(self):
        td_file = cons.TD_FILE_1
        project = Project()
        project.upload_td(td_file)



