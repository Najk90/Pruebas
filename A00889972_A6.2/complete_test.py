"""
Unit tests for the complete system.

Author: Najk
Date: 16-02-2024.
"""

import unittest
from test.test_hotel import TestHotelMethods
from test.test_customer import TestCustomerMethods
from test.test_reservation import TestReservationMethods
from test.test_file_manager import TestFileManagerMethods
from test.action_test import TestFileManagerActions


def suite():
    """Create a test suite that includes all test cases."""
    test_suite = unittest.TestSuite()
    test_suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(TestHotelMethods)
    )
    test_suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(TestCustomerMethods)
    )
    test_suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(TestReservationMethods)
    )
    test_suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(TestFileManagerMethods)
    )
    test_suite.addTest(
        unittest.TestLoader().loadTestsFromTestCase(TestFileManagerActions)
    )
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
