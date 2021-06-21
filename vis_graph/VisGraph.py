import networkx as nx
import numpy as np

class VisGraph:
    
    def __init__(self, time, mag, directed = None):
        
        self.time = np.array(time)
        self.mag = np.array(mag)

        if directed == True:
            self.graph = nx.DiGraph()
            self.directed = True
        else:
            self.graph = nx.Graph()
            self.directed = False
        
        if self.time.ndim != 1 or self.mag.ndim != 1:
            raise ValueError("One or both of the inputs are not one-dimensional")
        
        if len(self.time) != len(self.mag):
            raise ValueError("Inputs are different length")
    
    def get_graph(self):
        edges = []
        if self.directed == True:
            for i in range(len(self.mag) - 1):
                if self.mag[i + 1] > self.mag[i] > 0:
                    edges.append([i + 1, i])
                else:
                    edges.append([i, i + 1])
            for i in range(len(self.mag)):
                for j in range(i + 2, len(self.mag), 1):
                    line = self.mag[j] + (self.mag[i] - self.mag[j]) * (self.time[j] - self.time[i + 1:j]) / (self.time[j] - self.time[i])
                    values = self.mag[i + 1:j]
                    if np.all(line - values > 0):
                        if self.mag[j] > self.mag[i]:
                            #self.graph.add_edge(j, i)
                            edges.append([j, i])
                        else:
                            #self.graph.add_edge(i, j)
                            edges.append([i, j])
        else:
            for i in range(len(self.mag) - 1):
                edges.append([i, i + 1])
            for i in range(len(self.mag)):
                for j in range(i + 2, len(self.mag), 1):
                    line = self.mag[j] + (self.mag[i] - self.mag[j]) * (self.time[j] - self.time[i + 1:j]) / (self.time[j] - self.time[i])
                    values = self.mag[i + 1:j]
                    if np.all(line - values > 0):
                        edges.append([i, j])
        self.graph.add_edges_from(edges)
                  
        return self.graph
