import math

class Equation():
	
	def __init__(self, a,b,c):
		if a==0:
			return None
		self.a = a
		self.b = b
		self.c = c

	def solve(self):	
		delta = self.b**2 - (4*self.a*self.c)
		if delta < 0:
		   return None
		if delta == 0:
		   return -self.b / (2*self.a)	  
		if delta > 0:
		   x1 = (-self.b - math.sqrt(delta))/(2*self.a)
		   x2 = (-self.b + math.sqrt(delta))/(2*self.a)
		   w1 = min(x1,x2)
		   w2 = max(x1,x2)
		   return(w1,w2)

#a*x^2 + b*x + c