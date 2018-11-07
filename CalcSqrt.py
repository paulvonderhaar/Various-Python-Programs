
#  File: CalcSqrt.py

#  Description:This program uses a while loop to find the square root of any given number, and then compares that value to the value given by the exponent function that python comes with

#  Student Name:Paul Vonder Haar

#  Student UT EID:pmv347

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created:2/28/2014

#  Date Last Modified:2/28/2014

def main():
	#Get number from user input
 num=int(input("Enter a positive number"))
  #define the first 2 guesses
 newGuess=1
 oldGuess=num/2
 #Set up a loop that will keep running until old guess and new guess are very near equal
 while(abs(newGuess-oldGuess)>=1.0e-6):
 	#I needed to use a placeholder here, because if I tried to change newGuess before oldGuess, the oldGuess value would be incorrect, and if I changed oldGuess before newGuess, then the value for newGuess would be incorrect
  placeHolder=(((num/oldGuess)+oldGuess)/2)
  oldGuess=newGuess
  newGuess=placeHolder
  #Find the value of the difference, and round it to a reasonable degree of certainty
 difference=abs(newGuess-(num**.5))
 difference=round(difference,6)
 print("Square root is", newGuess)
 print("Difference is:",difference)
main()