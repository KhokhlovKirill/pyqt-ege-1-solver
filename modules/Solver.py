from itertools import *

class Solver:
    def __init__(self, matrix, graph):
        modified_graph = []
        for item in sorted(graph.keys()):
            modified_graph.append(''.join(graph[item]))

        modified_matrix = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                modified_matrix[(i+1, j+1)] = matrix[i][j]
        self.__graph = modified_graph
        self.__matrix = modified_matrix


    def solve(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s = ''
        for i in range(len(self.__graph)):
            s += alphabet[i]
            s += ''.join(sorted(self.__graph[i]))
            s += ' '
        s = s.strip()
        edges = set()
        for edge in self.__matrix:
            if self.__matrix[edge] is not None:
                edges.add(tuple(edge))
        d = dict()
        for edge in edges:
            if edge[0] not in d:
                d[edge[0]] = str(edge[1])
            else:
                d[edge[0]] += str(edge[1])
        z = ''
        for item in d:
            z += str(item) + str(d[item]) + ' '

        for x in permutations(set(s) - {' '}):
            t = z
            for a, b in zip(''.join(map(str, range(1, len(self.__graph)+1))), x):
                t = t.replace(a, b)

            g = ' '.join(c + ''.join(sorted(v)) for c, *v in sorted(t.split()))
            if g == s:
                return ''.join(x)