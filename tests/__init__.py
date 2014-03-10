# tests
# Test module for sbloc
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Mar 10 12:04:38 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Test module for sbloc
"""

##########################################################################
## Imports
##########################################################################

import unittest

##########################################################################
## Initialization Tests
##########################################################################

class InitializationTests(unittest.TestCase):

    def test_simple(self):
        """
        Assert that the world is sane by testing a simple world fact
        """
        self.assertEqual(2+2, 4)
