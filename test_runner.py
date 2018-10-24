import unittest
<<<<<<< HEAD
from tests import (test_index, test_login, test_session_persistence, test_logout)
=======
from tests import (test_index, test_login, test_session_persistence, test_rounds, test_rounds_races)
>>>>>>> round-page
import xmlrunner
import sys

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_index))
suite.addTests(loader.loadTestsFromModule(test_session_persistence))
suite.addTests(loader.loadTestsFromModule(test_login))
suite.addTests(loader.loadTestsFromModule(test_logout))
suite.addTests(loader.loadTestsFromModule(test_rounds))
suite.addTests(loader.loadTestsFromModule(test_rounds_races))

# initialize a runner, pass it your suite and run it
# runner = unittest.TextTestRunner(verbosity=3)
runner = xmlrunner.XMLTestRunner(verbosity=3, output='test-reports/unittest')

ret = not runner.run(suite).wasSuccessful()
sys.exit(ret)
