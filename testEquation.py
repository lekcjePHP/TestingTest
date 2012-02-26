import unittest
from equation import Equation 

class TestEquation(unittest.TestCase):
	def setUp(self): # metoda ktora sluzy do inicjalizacji zmiennych
		self.eq_no_result=Equation(1,2,3)
		self.eq_one_result = Equation(1,2,1)
		self.eq_two_result = Equation(1,-2,-15)
		self.eq_zero_all = Equation(0,0,0)

	def testNoResult(self):#metoda do testowania czy nasza klasa dziala poprawnie jak nie ma wynikow	
		wynik = self.eq_no_result.solve()
		self.assertEqual(wynik, None)
		
	def testOneResult(self):#metoda do tesotwania czy nasz klasa dziala poprawnie jak jest jedno rozwiaznaie
		wynik = self.eq_one_result.solve()
		self.assertEqual(wynik, -1)

	def testTwoResult(self):#
		wynik = self.eq_two_result.solve()
		self.assertEqual(wynik,(-3,5))

	def testZeroArgs(self):
		self.assertEqual(True, True)

unittest.main()