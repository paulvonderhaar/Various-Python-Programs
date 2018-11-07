
#  File: Day.py

#  Description:Uses an algorithm to determine the day of the week

#  Student Name:Paul Vonder Haar

#  Student UT EID:pmv347

#  Course Name: CS 303E

#  Unique Number: 53465

#  Date Created:2/17/14

#  Date Last Modified:2/17/14


def main():
 year=int(input("Enter Year: "))
 print(year)
 day=int(input("Enter day: "))
 print(day)
 month=int(input("Enter month: "))-2
 print(month)
 if month<1:
  month+=12
  year=year-1
 a=month
 print (a)
 b=day
 print(b)
 c=year%100
 print(c)