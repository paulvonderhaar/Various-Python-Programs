import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0):
    self.x=x
    self.y=y

  # get distance to another Point object
  def dist (self, other):
    return(math.hypot(abs(self.x-other.x),abs(self.y-other.y)))

  # create a string representation of a Point (x, y)
  def __str__ (self):
    return(str(self.x)+" "+str(self.y))
  # test for equality between two points
  def __eq__ (self, other):
    tol=1.9e-15
    return(abs(self.x-other.x) and abs(self.y-other.y))
class Line (object):
  # constructor assign default values if user defined points are the same
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    self.p1_x=(p1_x)
    self.p1_y=(p1_y)
    self.p2_x=(p2_x)
    self.p2_y=(p2_y)
  # determine if line is parallel to x axis
  def is_parallel_x (self):
    tol=1.9e-15
    return(abs(self.p1_x-self.p2_x)<tol)
  # determine if line is parallel to y axis
  def is_parallel_y (self):
    tol=1.9e-15
    return(abs(self.p1_y-self.p2_y)<tol)
  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
  def slope (self):
    if(self.is_parallel_y()):
      return(float("inf"))
    else:
      return((self.p1_x-self.p2_x)/(self.p1_y-self.p2_y))
  # determine the y-intercept of the line
  def y_intercept (self):
    return(self.p1_y-self.slope()*self.p1_x)
  # determine the x-intercept of the line
  def x_intercept (self):
    #x=-b/m if y=0
    if(self.is_parallel_x()):
      return("No x intercept")
    return(self.y_intercept()*-1/self.slope())
  # determine if two lines are parallel
  def is_parallel (self, other):
    tol=1.9e-15
    return(abs(self.slope()-other.slope())<tol)
  # determine if two lines are perpendicular to each other
  def is_perpendicular (self, other):
    return(other.slope()==-1/self.slope())
  # determine if a point is on the line or on an extension of it
  def is_on_line (self, p):
    return(p.y==self.y_intercept()+(self.slope()*p.x))
  # determine the perpendicular distance of a point to the line
  def perp_dist (self, p):
    if(self.is_on_line(p)):
      return(0)
    else:
      x=self.p1_x+self.slope()
      y=self.p1_y+self.slope()
      deltaX=x-p.x
      deltaY=y-p.y
      return(math.hypot(deltaX,deltaY))
    #This one is tricky, we need to define the point on the line closest to p
  # determine the intersection point of two lines if not parallel
  def intersection_point (self, other):
    if(self.is_parallel(other)):
      return("The points a parallel")
    else:
      interX=((self.y_intercept()-other.y_intercept())/(other.slope()-self.slope()))
      interY=(self.slope()*interX+self.y_intercept())
      return(Point(interX,interY))

  # determine if two points are on the same side of the line
  # return False if one or both points are on the line
  def on_same_side (self, p1, p2):
    result=False
    if(p1.y>=((self.slope()*self.p1_x)+self.y_intercept()) and p2.y>=((self.slope()*self.p1_x)+self.y_intercept())):
      result=True
    if(not(p1.y>=((self.slope()*self.p1_x)+self.y_intercept())) and not(p2.y>=((self.slope()*self.p1_x)+self.y_intercept()))):
      result=True
    return(result)
  # string representation of the line - one of three cases
  # y = c
  # x = c
  # y = m * x + b
  def __str__ (self):
    if(self.is_parallel_x):
      return("y = "+str(self.p2_x))
    elif(self.is_parallel_y):
      return("x = "+str(self.p1_y))
    else:
      return(str(self.p1_y)+" = "+str(self.slope())+" "+str(self.p1_x)+" "+str(self.y_intercept))
class Circle (object):
  # constructor with default values
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius=radius
    self.center=Point(x,y)
  # compute circumference
  def circumference (self):
    return(math.pi*2*self.radius)
  # compute area
  def area (self):
    return(math.pi*self.radius**2)
  # determine if a point is inside the circle
  def is_inside_point (self, p):
    return(math.hypt(abs(p.x-self.center.x),abs(p.y-self.center.y)<self.radius))
  # determine if the other circle is strictly inside self
  def is_inside_circle (self, other):
    return(self.center.dist(other.center)+other.radius<self.radius)
  # determine if the other circle intersects self
  def does_intersect_circle (self, other):
    return(math.hypot(abs(self.center.x-other.center.x),abs(self.center.y-other.center.y))<=self.radius+other.radius)
  # determine if the line intersects circle
  def does_intersect_line (self, line):
    return(line.perp_dist(self.center)<self.radius)
  # determine if the line is tangent to the circle
  def is_tangent (self, line):
    return(line.perp_dist(self.center)==self.radius)
  # string representation of a circle
  # Radius: radius, Center: (x, y)
  def __str__ (self):
    return("Radius: "+str(self.radius)+", Center: ("+str(self.center)+")")
def main():
  # open file "geometry.txt" for reading
  inFile=open("geometry.txt","r")
  # read the coordinates of the first Point P
  inLine=inFile.readline()
  coordinates=inLine.split(" ", 1)
  pointP=Point(float(coordinates[0]),float(coordinates[1]))
  # read the coordinates of the second Point Q
  inLine=inFile.readline()
  coordinates=inLine.split(" ", 1)
  pointQ=Point(float(coordinates[0]),float(coordinates[1]))  
  # print the coordinates of points P and Q
  print("Coordinates of P: "+str(pointP))
  print("Coordinates of Q: "+str(pointQ))

  # print distance between P and Q
  print("Distance between P and Q: "+str(pointP.dist(pointQ)))
  # print the slope of the line PQ
  linePQ=Line(pointP.x,pointP.y,pointQ.x,pointQ.y)
  print("Slope of PQ: "+str(linePQ.slope()))
  # print the y-intercept of the line PQ
  print("Y-Intercept of PQ:"+str(linePQ.y_intercept()))
  # print the x-intercept of the line PQ
  print("X-Intercept of PQ: "+str(linePQ.x_intercept()))
  # read the coordinates of the third Point A
  inLine=inFile.readline()

  coordinates=inLine.split(" ", 1)
  pointA=Point(float(coordinates[0]),float(coordinates[1]))
  # read the coordinates of the fourth Point B
  inLine=inFile.readline()

  coordinates=inLine.split(" ", 1)
  pointB=Point(float(coordinates[0]),float(coordinates[1]))
  # print the string representation of the line AB
  lineAB=Line(pointA.x,pointA.y,pointB.x,pointB.y)
  print("Line AB: "+str(lineAB))

  # print if the lines PQ and AB are parallel or not
  if(linePQ.is_parallel(lineAB)):
    print("PQ is parllel to AB")
  else:
    print("PQ is not parallel to AB")
  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if(linePQ.is_perpendicular(lineAB)):
      print("PQ is perpendicular to AB")
  else:
    print("PQ is not perpendicular to AB") 
  # print coordinates of the intersection point of PQ and AB if not parallel
  if(not linePQ.is_parallel(lineAB)):
    print("Intersection point of PQ and AB: "+str(linePQ.intersection_point(lineAB)))
  # read the coordinates of the fifth Point G
  inLine=inFile.readline()
  coordinates=inLine.split()
  pointG=Point(float(coordinates[0]),float(coordinates[1]))  
  # read the coordinates of the sixth Point H
  inLine=inFile.readline()
  coordinates=inLine.split()
  pointH=Point(float(coordinates[0]),float(coordinates[1]))
  # print if the the points G and H are on the same side of PQ
  if(linePQ.on_same_side(pointH,pointG)):
    print("G and H are on the same side of PQ")
  else:
    print("G and H are not on the same side of PQ")
  # print if the the points G and H are on the same side of AB
  if(lineAB.on_same_side(pointH,pointG)):
    print("G and H are on the same side of AB")
  else:
    print("G and H are not on the same side of AB")
  # read the radius of the circleA and the coordinates of its center
  inLine=inFile.readline()
  coordinates=inLine.split()
  circleA=Circle(float(coordinates[0]),float(coordinates[1]),float(coordinates[2]))
  # read the radius of the circleB and the coordinates of its center
  inLine=inFile.readline()
  coordinates=inLine.split()
  circleB=Circle(float(coordinates[0]),float(coordinates[1]),float(coordinates[2]))
  # print the string representation of circleA and circleB
  print("circleA: "+str(circleA))
  print("circleB:"+str(circleB))

  # determine if circleB is inside circleA
  if(circleB.is_inside_circle(circleA)):
    print("circleB is inside circleA")
  else:
    print("circleb is not inside circleB")
  # determine if circleA intersects circleB
  if(circleA.does_intersect_circle(circleB)):
    print("circleA does intersect circleB")
  else:
    print("circleA does not intersect circleB")
  # determine if line PQ (or extension) intersects circleA
  if(circleA.does_intersect_line(linePQ)):
    print("PQ does intersect circle A")
  else:
    print("PQ does not interesect circle A")
  # determine if line AB (or extension) is tangent to circleB
  if(circleA.is_tangent(lineAB)):
    print("AB is a tangent to circle B")
  else:
    print("AB is not a tangent to circleB")
  # close file "geometry.txt"
  inFile.close()
main()