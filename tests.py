import unittest

from brain import Brain
from signals import *	

class MemoryTests(unittest.TestCase):
	def setUp(self):
		print "next"
		self.b = Brain()
		self.dummy_signals = [Pain(1.0), Color(255,0,0), Color(5,10,115), Incentive(0.5), Color(255,255,255)]

	def test_same_long_term_memory_difference_equal_to_zero(self):
		""" Tests that two equivalent Long Term Memories have a difference of zero """

		signals = self.dummy_signals
		m1 = Long_Term_Memory(signals)
		m2 = Long_Term_Memory(signals)

		difference1 = m1.difference(m2)

		self.assertEqual(difference1, 0)

	def test_long_term_memory_difference_signal_order(self):
		""" Tests that two equivalent Long Term Memories have the same difference if their signals are reversed """

		signals = self.dummy_signals
		m1 = Long_Term_Memory(signals)
		signals.reverse()
		m2 = Long_Term_Memory(signals)

		difference1 = m1.difference(m1)
		difference2 = m1.difference(m2)

		self.assertEqual(difference1, difference2)

	def test_long_term_memory_difference_order_of_call(self):
		""" Tests that two equivalent Long Term Memories have the same difference if called in reverse order """

		signals = self.dummy_signals
		m1 = Long_Term_Memory(signals)
		m2 = Long_Term_Memory(signals)

		difference1 = m1.difference(m2)
		difference2 = m2.difference(m1)

		self.assertEqual(difference1, difference2)




def main():
	unittest.main()

if __name__ == "__main__":
	main()