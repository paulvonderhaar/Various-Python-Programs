
#  File: CalculatePI.py

#  Description:This program is designed to find the value of Pi using a very novel method. This program simulates a square dartboard with a circular target. A dart is then fired randomly so that it hits
# the square in a random place many times. Then the program takes the number of darts that landed inside the circle, divides it byt he number of darts thrown total, and sets that proportion equal to Pi/4, and solves for Pi.

#  Student Name:Paul Vonder Haar

#  Student UT EID:pmv347

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created:3/23/14

#  Date Last Modified:3/24/14
#import math and random
import math
import random

#Input a number, and Pi will be computed using that many random throws
def computePI(numThrows):
	#A counter of how many random darts would land in the circle with radius 1
	inCircle=0
	#does the number equal to the input
	for i in range(0,numThrows):
		#Creates a random point inside the square
		xPos=random.uniform(-1.0,1.0)
		yPos=random.uniform(-1.0,1.0)
		#checks to see if that point will be inside the circle, using the pythagorean theorum, and increments inCircle if it is
		if(math.hypot(xPos,yPos)<=1):
			inCircle+=1
		#Finds the proportion of the number of circles over the number of throws, and then multiplies it by 4, because inCircle/total = pi/4
	return(4.0*(inCircle/numThrows))

def main():
	 print("Computation of PI using Random Numbers")
	 num=10
	 #Runs the test 6 times
	 for p in range (0,6):
	 	#Every time, 10 times more tests are done, if the numbers are truly random, then with a larger num, the value of pi should be close to the real value
	 	num=num*10
	 	#Calculates pi using num tosses
	 	compPi=computePI(num)
	 	#compares the value calculated from comp pi, to the value given by math.pi
	 	difference=compPi-math.pi
	 	print("num = %.8d       CalculatedPi =%.7f    Difference =%.7f "%(num,compPi,difference))
main()