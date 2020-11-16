import sys

class Vertex:

	# color is some number, with 0 being uncolored
	def __init__(self, name, color=0):
		self.name = name
		self.color = color

	def __repr__(self):
		return str(self.name)

class Edge:
	def __init__(self, v1, v2, weight=1):
		self.v1 = v1
		self.v2 = v2
		self.weight = weight

	def __repr__(self):
		return "\nedge: " + self.v1.name + ":" + str(self.v1.color) + " " + self.v2.name + ":" + str(self.v2.color) + " weight:" + str(self.weight)

class Graph:

	# V is set of vertices, E is set of edges
	def __init__(self, V, E):
		self.V = V
		self.E = E

	def __repr__(self):
		string = ""
		for edge in self.E:
			string += str(edge)
		return string

	def Neighbors(self, v):
		adjacents = set()
		for edge in self.E:
			if edge.v1 == v:
				adjacents.add(edge.v2)
			elif edge.v2 == v:
				adjacents.add(edge.v1)
		return adjacents

	def MinEdge(self, v):
		# largest integer value
		min_weight = sys.maxsize
		min_edge = None
		for edge in self.E:
			if edge.weight < min_weight:
				min_weight = edge.weight
				min_edge = edge
		return min_edge

	def RemoveEdge(self, e):
		self.E.remove(e)

	def RemoveVertex(self, v):
		self.V.remove(v)
		for edge in self.E:
			if edge.v1 == v or edge.v2 == v:
				self.E.remove(edge)

	def ChromaticNumber(self):
		num_distinct = set()
		for vertex in self.V:
			if vertex.color == 0:
				print("lmao ur bad the graph isn't done coloring yet")
				return None
			else:
				num_distinct.add(vertex.color)
		return len(num_distinct)

	def IsValidColoring(self):
		for edge in self.E:
			if edge.v1.color == 0 or edge.v2.color == 0:
				print("lmao ur bad the graph isn't done coloring yet")
				return None
			if edge.v1.color == edge.v2.color:
				return False
		return True

	def GreedyColor(self):
		for vertex in self.V:
			distinct_colors = set()
			adjacents = self.Neighbors(vertex)
			for adj in adjacents:
				distinct_colors.add(adj.color)
			for i in range(1,len(self.V)):
				if i not in distinct_colors:
					vertex.color = i
					break

	# not done
	def BruteForce(self):
		for i in range(len(self.V)):
			for vertex in self.V:
				distinct_colors = set()
				adjacents = self.Neighbors(vertex)

	# Optional problems!!

	def DFS(self, start_vertex, target_vertex):
		pass

	def IsTree(self):
		pass

	def IsPlanar(self):
		pass

	# next(iter(set()))
	def SpanningTree(self):	
		discovered = set()
		T = set()
		node = next(iter(self.V))
		frontier = [node]
		while frontier:
			if 



		

vert = Vertex("a")
ver = Vertex("b")
ve = Vertex("c")
v = Vertex("d")
ed = Edge(vert, ver, 42)
edg = Edge(v, ver, 7)
edgy = Edge(ver, ve)

print(vert)
print(ed)
print(edgy)
V = {vert, ver, ve, v}
E = {ed, edg, edgy}
gra = Graph(V, E)
print(gra.Neighbors(ve))
print(gra.MinEdge(ver))
print(gra.ChromaticNumber())
print(gra.IsValidColoring())
gra.GreedyColor()
print(gra)


'''
Create an empty collection of edges T (our tree, to be filled in by our algorithm).
Keep some auxiliary data structures to track which nodes we've seen already. 
Start with any vertex. Insert it into a frontier data structure. While the frontier is non-empty, 
Pop a vertex v from the frontier. 
If we haven't seen v before, mark it as visited.
Identify all of the neighbors of v, let these be [n1, n2, … ]
For each unvisited neighbor ni, insert into T an edge from v to ni.
Add ni to the frontier.
When the frontier is empty, we have explored all the nodes, and our T data structure contains a subset of the edges needed to make a spanning tree.

Implement this algorithm as a method on your graph class. It should return a set of edge objects from the original graph. This code should look very familiar...
'''
def SpanningTree(self):
	T = []
	frontier = self.V
	discovered = []
	start = self.V[1]
	while len(frontier) is not 0:
		point = frontier.pop(1)
		if point not in discovered:
			discovered.append(point)
			neighbors = point.Neighbors
			for i in Neighbors:
				if i is not in discovered:
					T.append(self.E)
# next(iter(set()))
	def SpanningTree(self):	
		discovered = set()
		T = set()
		node = next(iter(self.V))
		frontier = [node]
		while frontier:
			if frontier[0] in discovered:
				frontier = [node] # go to the next vertex? how? sets?
			frontier.pop()
			else:
				discovered.add(frontier[0])
				T.add(MinEdge(frontier[0]))			
				frontier = next(frontier)


def DFS(state):
	frontier = [(0, state)]
	discovered = set([state])
	parents = {(0, state): None}
	path = []
	while len(frontier) != 0:
		current_state = frontier.pop(0)
		discovered.add(current_state[1])
		if IsGoal(current_state[1]):
			while parents.get((current_state[0], current_state[1])) != None:
				path.insert(0, current_state[0])
				current_state = parents.get((current_state[0], current_state[1]))
			return path
		for neighbor in ComputeNeighbors(current_state[1]):
			if neighbor[1] not in discovered:
				frontier.insert(0, neighbor)
				discovered.add(neighbor[1])
				parents.update({(neighbor[0], neighbor[1]): current_state})
	print("--FAIL--")
	return None



	
