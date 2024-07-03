import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """
  def test_get_ratio(self):
    ratio_a_1 = 3
    ratio_a_2 = 4
    ratio_b_1 = 2
    ratio_b_bad = 0
    res_a1_bbad = None
    res_a1_b1 = (ratio_a_1 / ratio_b_1)
    res_a2_b_1 = (ratio_a_2 / ratio_b_1)
    self.assertEqual(getRatio(ratio_a_1,ratio_b_1), res_a1_b1)
    self.assertEqual(getRatio(ratio_a_2, ratio_b_1), res_a2_b_1)
    self.assertEqual(getRatio(ratio_a_1, ratio_b_bad), res_a1_bbad)


if __name__ == '__main__':
    unittest.main()
