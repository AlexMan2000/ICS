class Graph:
    def __init__(self,graph):
        self._graph_dict = graph


    def vertices(self):
        return list(self._graph_dict.keys())

    def neighbours(self,key):
        return self._graph_dict[key]


    def edges(self):
        res = []
        for k,v in self._graph_dict:
            for i in range(len(v)):
                if {k,v[i]} not in res:
                    res.append({k,v[i]})
        return res


    def add_vertex(self,vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []
        else:
            print('{} has already been in the graph'.format(vertex))


    def add_edge(self,vertice1,vertice2):
        if vertice1 not in self._graph_dict:
            self.add_vertex(vertice1)
            self._graph_dict[vertice2].append(vertice1)
        if vertice2 not in self._graph_dict:
            self.add_vertex(vertice2)
            self._graph_dict[vertice1].append(vertice2)
        if not (vertice1 in self._graph_dict or vertice2 in self._graph_dict):
            self.add_vertex(vertice1)
            self.add_vertex(vertice2)
            self._graph_dict[vertice1].append(vertice2)
            self._graph_dict[vertice2].append(vertice1)
        if vertice1 in self._graph_dict and vertice2 in self._graph_dict:
            self._graph_dict[vertice1].append(vertice2)
            self._graph_dict[vertice2].append(vertice1)


    def remove_edge(self,vertice1,vertice2):
        if {vertice1,vertice2} in self.edges():
            self._graph_dict[vertice1].remove(vertice2)
            self._graph_dict[vertice2].remove(vertice1)



    def remove_vertex(self,vertex):
        if vertex in self._graph_dict.keys():
            del self._graph_dict[vertex]
        for k,v in self._graph_dict:
            if vertex in v:
                self._graph_dict[k].remove(vertex)

fig1 = {'a':['b','c','d'],'b':['a','d'],'c':['a','d'],'d':['a','b','c'],'e':['f'],'f':['e']}
graph = Graph(fig1)
def trace_contact(graph,vertex,component):
    def helper(vertex_list,vertex):
        for item in [vertex]+vertex_list:
            if item in component:
                continue
            else:
                component.append(item)
                helper(graph._graph_dict[item],item)

    helper(graph._graph_dict[vertex],vertex)
    return component

print(trace_contact(graph,'a',[]))

























