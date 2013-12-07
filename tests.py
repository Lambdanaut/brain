import unittest

from brain import Brain
from signals import *	

class MemoryTests(unittest.TestCase):
	def setUp(self):
		self.b = Brain()
		self.dummy_signals1 = [Pain(1.0), Color(255,0,0), Color(5,10,115), Incentive(0.5), Color(255,255,255)]
		self.dummy_signals2 = [Color(0,0,0), Color(0,100,255), Incentive(1.0), Incentive(1.0)]

	def test_same_ltm_difference_equal_to_zero(self):
		""" Tests that two equivalent Long Term Memories have a difference of zero """

		signals = self.dummy_signals1
		m1 = Long_Term_Memory(signals)
		m2 = Long_Term_Memory(signals)

		difference1 = m1.difference(m2)

		self.assertEqual(difference1, 0)

	def test_ltm_difference_signal_order(self):
		""" Tests that two equivalent Long Term Memories have the same difference if their signals are reversed """

		signals = self.dummy_signals1
		m1 = Long_Term_Memory(signals)
		signals.reverse()
		m2 = Long_Term_Memory(signals)

		difference1 = m1.difference(m1)
		difference2 = m1.difference(m2)

		self.assertEqual(difference1, difference2)

	def test_ltm_difference_order_of_call(self):
		""" Tests that two different Long Term Memories have the same difference if called in reverse order """
		
		signals1 = self.dummy_signals1
		signals2 = self.dummy_signals2
		m1 = Long_Term_Memory(signals1)
		m2 = Long_Term_Memory(signals2)

		difference1 = m1.difference(m2)
		difference2 = m2.difference(m1)

		self.assertEqual(difference1, difference2)

	def test_ltm_equal_combined(self):
		""" Tests that two equivalent Long Term Memories have equal signal lists regardless of the order they are combined in """

		signals1 = self.dummy_signals1
		signals2 = self.dummy_signals2
		m1 = Long_Term_Memory(signals1)
		m2 = Long_Term_Memory(signals2)

		combined1 = m1.combine(m2)
		combined2 = m2.combine(m1)

		self.assertEqual(combined1.signals, combined2.signals)

class SignalTests(unittest.TestCase):
	def setUp(self):
		pass 

	def test_color_difference(self):
		""" Tests that the difference of the same two colors is 0 """
		red = Color(255,0,0)
		self.assertEqual(red.difference(red), 0.0)


def main():
	unittest.main()

if __name__ == "__main__":
	main()