import unittest
from tests import (test_index)
import xmlrunner
import sys

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_index))

# initialize a runner, pass it your suite and run it
# runner = unittest.TextTestRunner(verbosity=3)
runner = xmlrunner.XMLTestRunner(verbosity=3, output='test-reports/unittest')

ret = not runner.run(suite).wasSuccessful()
sys.exit(ret)