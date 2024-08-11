import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      expected_stock = quote['stock']
      expected_ask = quote['top_ask']['price']
      expected_bid = quote['top_bid']['price']
      expected_price = (expected_ask+expected_bid)/2
      self.assertEqual(stock,expected_stock)
      self.assertEqual(bid_price,expected_bid)
      self.assertEqual(ask_price,expected_price)
      self.assertEqual(price,expected_price)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock, bid_price, ask_price, price = getDataPoint(quote)
    expected_stock = 'ABC'
    expected_ask = 119.2
    expected_bid = 120.48
    expected_price = (expected_ask+expected_bid)/2
    self.assertEqual(stock,expected_stock)
    self.assertEqual(bid_price,expected_bid)
    self.assertEqual(ask_price,expected_price)
    self.assertEqual(price,expected_price)
  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceBidLessThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock, bid_price, ask_price, price = getDataPoint(quote)
    expected_stock = 'DEF'
    expected_ask = 121.68
    expected_bid = 117.87
    expected_price = (expected_ask+expected_bid)/2
    self.assertEqual(stock,expected_stock)
    self.assertEqual(bid_price,expected_bid)
    self.assertEqual(ask_price,expected_price)
    self.assertEqual(price,expected_price)


if __name__ == '__main__':
    unittest.main()
