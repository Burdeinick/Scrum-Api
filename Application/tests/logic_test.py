import unittest
import sys
sys.path.insert(0, 'Application')
from scripts.logic.logic import SumEstimation


class TestSumEstimation(unittest.TestCase):
    """"This class for the testing of logic.""" 
    def setUp(self):
        self.sum_1 = SumEstimation('100h')  
        self.sum_2 = SumEstimation('55555500h') 

    def test_1(self):
        print(self.sum_1.response)
        self.assertEqual(self.sum_1.response, '2w2d4h')

    def test_1(self):
        print(self.sum_1.response)
        self.assertEqual(self.sum_2.response, '347221m3w2d4h')


def test_server_run():
    unittest.main()

test_server_run()