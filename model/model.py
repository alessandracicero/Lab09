import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo=nx.Graph()
        self._idMapA= {}
        for aeroporto in DAO.getAeroporti():
            self._idMapA[aeroporto.ID]=aeroporto

    def buildGraph(self, distMin):
        flights = DAO.getDistMin(distMin)
        self._grafo.clear()

        for flight in flights:
            o = self._idMapA[flight.ORIGIN_AIRPORT_ID]
            d = self._idMapA[flight.DESTINATION_AIRPORT_ID]

            self._grafo.add_node(o)
            self._grafo.add_node(d)
            self._grafo.add_edge(o, d,weight=flight.DISTANCE)
            #self._grafo.add_edge(d, o,weight=flight.DISTANCE)

    def getNumNodi(self):
        return len(self._grafo.nodes())

    def getNumArchi(self):
        return len(self._grafo.edges())

    def getArchiPeso(self):
        res = []
        for o,d,p in self._grafo.edges(data=True):
            peso = p.get('weight')
            res.append((o,d,peso))
        res.sort(key=lambda x: x[2])
        return res

