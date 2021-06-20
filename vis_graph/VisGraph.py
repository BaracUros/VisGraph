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
        
        for i in range(len(self.time)):
            for j in range(i + 1, len(self.time), 1):
                
                if j == i + 1:
                    if self.directed == True:
                        if self.mag[i] > self.mag[j]:
                            self.graph .add_edge(i, j)
                        elif self.mag[i] == self.mag[j]:
                            self.graph .add_edge(i, j)
                        else:
                            self.graph .add_edge(j, i)
                    else:
                        self.graph .add_edge(i, j)
                else:
                    connect = True
                    if self.directed == True:
                        for k in range(i +1, j, 1):
                            if self.mag[k] > self.mag[j] + (self.mag[i] - self.mag[j]) * (self.time[j] - self.time[k]) / (self.time[j] - self.time[i]):
                                connect = False
                                break
                        if connect == True:
                            if self.mag[i] > self.mag[j]:
                                self.graph .add_edge(i, j)
                            elif self.mag[i] == self.mag[j]:
                                self.graph .add_edge(i, j)
                            else:
                                self.graph .add_edge(j, i)
                    else:
                        for k in range(i +1, j, 1):
                            if self.mag[k] > self.mag[j] + (self.mag[i] - self.mag[j]) * (self.time[j] - self.time[k]) / (self.time[j] - self.time[i]):
                                connect = False
                                break
                        if connect == True:
                            self.graph .add_edge(i, j)
        return self.graph


