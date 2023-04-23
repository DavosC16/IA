import math

class node:
	def __init__(self, i, h = 0):
		self.id = i #identificador
		self.heuristica = h #valor de la heuristica del nodo
		self.neighbor = [] #lista de nodos conectados al nodo i
		self.visited = False #saber si el nodo ya fue visitado
		self.father = None	#nodo visitado con anterioridad
		self.cost = float('inf')	#valor de recorrer ese nodo
		self.costF = float('inf')

	def addNeighbor(self, v, p = 0):
		if v not in self.neighbor:
			self.neighbor.append([v, p])

class graph:
	def __init__(self):
		self.nodes={}

	def addNode(self, id):
		if id not in self.nodes:
			self.nodes[id]=node(id)

	def addEdge(self, a, b, c):
		if a in self.nodes and b in self.nodes:
			self.nodes[a].addNeighbor(b,c)
			self.nodes[b].addNeighbor(b,c)			
	
	def path(self, a, b):
		path=[]
		current=b
		while current!=None:
			path.insert(0,current)
			current=self.nodes[current].father
		return path

	def minH(self, l):
		if len(l) > 0:
			m = self.nodes[l[0]].costF
			v = l[0]
			for e in l:
				if m > self.nodes[e].costF:
					m = self.nodes[e].costF
					v = e
			return v
		return v

	def aStar(self, a, b):
		if a in self.nodes and b in self.nodes:
			
			self.nodes[a].cost = 0
			self.nodes[a].costF = self.nodes[a].heuristica

			for v in self.nodes:
				if v != a:
					self.nodes[v].cost = float('inf')
					self.nodes[v].costF = float('inf')
				self.nodes[v].padre = None

			abierto = [a]

			while len(abierto) > 0:
				current = self.minH(abierto)

				if current == b:
					return [self.path(a, b), self.nodes[b].cost]

				abierto.remove(current)
				self.nodes[current].visited = True

				for v in self.nodes[current].neighbor:
					if self.nodes[v[0]].visited == False:
						if self.nodes[v[0]].id not in abierto:
							abierto.append(v[0])
						if self.nodes[current].cost + v[1] < self.nodes[v[0]].cost:
							self.nodes[v[0]].father = current
							self.nodes[v[0]].cost = self.nodes[current].cost + v[1]
							self.nodes[v[0]].costF = self.nodes[v[0]].cost + self.nodes[v[0]].heuristica
			return False
		else:
			return False