class node:
    def __init__(self,i):
        self.id=i
        self.neighbor=[]
        self.visited=False
        self.father=None
        self.cost=float('inf')

    def addNeighbor(self, e, c):
        if e not in self.neighbor:
            self.neighbor.append([e,c])

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

    def min(self, list):
        if len(list)>0:
            m=self.nodes[list[0]].cost
            n=list[0]
            for i in list:
                if m>self.nodes[i].cost:
                    m=self.nodes[i].cost
                    n=i
            return n
    
    def dijkstra(self, a):
        self.nodes[a].cost=0
        currentNode=a
        notVisited = []

        for i in self.nodes:
            if i!=a:
                self.nodes[i].cost=float('inf')
            self.nodes[i].father=None
            notVisited.append(i)

        while len(notVisited)>0:
            for j in self.nodes[currentNode].neighbor:
                if self.nodes[j[0]].visited==False:
                    if self.nodes[currentNode].cost + j[1] < self.nodes[j[0]].cost:
                        self.nodes[j[0]].cost = self.nodes[currentNode].cost+j[1]
                        self.nodes[j[0]].father = currentNode
            
            self.nodes[currentNode].visited=True
            notVisited.remove(currentNode)

            currentNode=self.min(notVisited)

    def path(self, a, b):
        path=[]
        current=b
        while current!=None:
            path.insert(0,current)
            current=self.nodes[current].father

        for i in path:
            print(i)
            if i!=b:
                print("-->")
            else:
                print('Costo = '+str(self.nodes[b].cost))

class main:
    g = graph()
    g.addNode(1)
    g.addNode(2)
    g.addNode(3)
    g.addNode(4)
    g.addEdge(1, 2, 1)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 3)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 4, 5)

    print("\nLa ruta es:")
    g.dijkstra(1)
    g.path(1, 4)