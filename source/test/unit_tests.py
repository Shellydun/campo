import unittest
import sys

import extract_const_diff
import extract_const_same
import extract_dyn_same
import extract_dyn_diff
import test_phenomenon
import test_propertyset


if __name__ == '__main__':

    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(extract_const_diff.TestConstDiff))
    #suite.addTest(unittest.makeSuite(extract_const_same.TestConstSame))
    #suite.addTest(unittest.makeSuite(extract_dyn_same.TestDynSame))
    #suite.addTest(unittest.makeSuite(extract_dyn_diff.TestDynDiff))
    suite.addTest(unittest.makeSuite(test_phenomenon.TestPhenomenon))
    suite.addTest(unittest.makeSuite(test_propertyset.TestPropertyset))

    result = unittest.TextTestRunner(verbosity=3).run(suite)
    test_result = (0 if result.wasSuccessful() else 1)

    sys.exit(test_result)
