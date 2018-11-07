#  File: Graph.py

#  Description:Create a number of functions that will allow us to transverse a graph

#  Student Name:Paul Vonder Haar

#  Student UT EID:pmv347


#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:


class Vertex(object):
	def __init__(self,label):
		self.label=label
		self.visited=False

	def wasVisited(self):
		return self.visited

	def getLabel(self):
		return(self.label)
	def __str(self):
		return(str(self.label))




class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))




class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)




class Graph(object):
	def __init__(self,):
		self.Vertices=[]
		self.adjMat=[]


	#Checks if a particular vertex is in the graph
	def hasVertex(self,label):
		for i in range(len(self.Vertices)):
			if(label==(self.Vertices[i]).label):
				return(True)
		return(False)

	def addVertex(self,label):
		if (not self.hasVertex(label)):
			self.Vertices.append(Vertex(label))
			for i in range(len(self.Vertices)-1):
				self.adjMat[i].append(0)
			newRow=[]
			for i in range(len(self.Vertices)):
				newRow.append(0)
			self.adjMat.append(newRow)

	def addDirectedEdge(self,start,finish,weight=1):
		self.adjMat[start][finish]=weight

	def getAdjUnivisitedVertex(self,v):
		nVert=len(self.Vertices)
		for i in range(nVert):
			if((self.adjMat[v][i]>0) and(not(self.Vertices[i].wasVisited()))):
				return i
		return(-1)

	def dfs(self,v):
		theStack=Stack()

		(self.Vertices[v]).visited=True
		print(self.Vertices[v].label)
		theStack.push(v)
		while(not theStack.isEmpty()):
			u=self.getAdjUnivisitedVertex(theStack.peek())
			if(u==-1):
				u=theStack.pop()
			else:
				(self.Vertices[u]).visited=True
				print(self.Vertices[u].label)
				theStack.push(u)

		nVert=len(self.Vertices)
		for i in range(nVert):
			(self.Vertices[i]).visited=False

	def getIndex(self,label):
		nVert=len(self.Vertices)
		for i in range(nVert):
			if(self.Vertices[i].label==label):
				return(i)
		return(-1)

	def bfs(self,v):
		theQueue=Queue()
		(self.Vertices[v]).visited=True
		print(self.Vertices[v].label)
		theQueue.enqueue(v)
		while(not theQueue.isEmpty()):
			v1=theQueue.dequeue()
			v2=self.getAdjUnivisitedVertex(v1)
			while(v2!=-1):
				(self.Vertices[v2]).visited=True
				print(self.Vertices[v2].label)
				theQueue.enqueue(v2)
				v2=self.getAdjUnivisitedVertex(v1)

	def getEdgeWeight(self,fromVertexLabel,toVertexLabel):
		fromVertIndex=self.getIndex(fromVertexLabel)
		toVertIndex=self.getIndex(toVertexLabel)
		if((self.adjMat[fromVertIndex][toVertIndex])==0):
			return(-1)
		else:
			return((self.adjMat[fromVertIndex][toVertIndex]))



	def getNeighbors(self,vertexLabel):
		vertexIndex=self.getIndex(vertexLabel)
		Indexanswer=[]
		answer=[]
		for i in range(len(self.adjMat[vertexIndex])):
			if(self.adjMat[vertexIndex][i]!=0):
				Indexanswer.append(i)

		for j in range(len(Indexanswer)):
			answer.append(self.Vertices[Indexanswer[j]].label)
		return(answer)

	def getVertices(self):
		answer=[]
		for i in range(len(self.Vertices)):
			answer.append(self.Vertices[i].label)
		return(answer)

	def hasCycle(self):
		for v in range(len (self.Vertices)):
			theStack=Stack()
			Answer=[]
			theStack.push(v)
			while(not theStack.isEmpty()):
				u=self.getAdjUnivisitedVertex(theStack.peek())
				if(u==v):
					return(True)
				if(u==-1):
					u=theStack.pop()
				else:
					(self.Vertices[u]).visited=True
					theStack.push(u)

			nVert=len(self.Vertices)
			for i in range(nVert):
				(self.Vertices[i]).visited=False
		return(False)

	def edgeList(self):
			weightList=[]
			VertexList=[]
			for i in range(len(self.adjMat)):
				for j in range(len(self.adjMat[i])):
					if(self.adjMat[i][j]!=0):
						weightList.append(self.adjMat[i][j])
						VertexList.append(self.Vertices[i].label+"--"+self.Vertices[j].label)

			for i in range(len(weightList)):
				minimum=i
				for j in range(i,len(weightList)):
					if(weightList[j]<weightList[minimum]):
						minimum=j
				temp=weightList[i]
				tempStr=VertexList[i]

				weightList[i]=weightList[minimum]
				VertexList[i]=VertexList[minimum]
				
				weightList[minimum]=temp
				VertexList[minimum]=tempStr

			for i in range(len(weightList)):
				print(VertexList[i]+" "+str(weightList[i]))

























def main():
	MyGraph=Graph()
	InData=open("graph.txt","r")
	numVert=int(InData.readline())

	for i in range(numVert):
		CurrentCity=InData.readline()
		CurrentCity=CurrentCity.strip()
		MyGraph.addVertex(CurrentCity)

	numEdges=int(InData.readline())
	
	for j in range(numEdges):
		temp=InData.readline()
		EdgeData=temp.split()
		MyGraph.addDirectedEdge(int(EdgeData[0]),int(EdgeData[1]),int(EdgeData[2]))
	
	city=InData.readline()
	cityIndex=MyGraph.getIndex(city)
	print("DFS from "+city+":")
	MyGraph.dfs(cityIndex)
	print()
	print("BFS from "+city+":")
	MyGraph.bfs(cityIndex)
	print()
	print("Topological Sort:")
	MyVertices=MyGraph.getVertices()
	for i in range(len(MyVertices)):
		print(MyVertices[i])

	print()
	print("Ascending Edges:")
	MyGraph.edgeList()




main()