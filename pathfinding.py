class Pathfinding:
    def astar(self, graph, start, goal, heuristic):
        # TODO
        pass

    def bfs(self, graph: dict, start, goal):
        """
        Find shortest path using Breadth-first search

        :params graph: adjaceny list
        """
        # initialize queue with starting node
        queue = [(start, [start])]
        # create an empty set to keep track of nodes visited
        visited = set()

        # iterate thru each node 
        while queue:
            # dequeue first element of the queue
            (node, path) = queue.pop(0)

            # if goal found
            if node == goal:
                return path
            
            if node not in visited:
                visited.add(node)

                # for each neighbor of hasn't been visited yet
                for neighbor in graph[node]:
                    # add (neighbor and path took to visit neighbor) to queue
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        # shortest path not found
        return None

# sample graphs
graphs = [
            ({
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "F", "G"],
            "D": ["B"],
            "E": ["B"],
            "F": ["C"],
            "G": ["C"],
            }, "A", "F"),

            ({
                1: {2: 4, 3: 5, 4: 4},
                2: {1: 4, 6: 2, 7: 2},
                3: {1: 5, 4: 3, 6: 1, 8: 8},
                4: {1: 4, 3: 3, 5: 5},
                5: {4: 5, 6: 3},
                6: {2: 2, 3: 1, 5: 3, 7: 1},
                7: {2: 2, 6: 1},
                8: {3: 8, 9: 1, 10: 3},
                9: {8: 1, 10: 1},
                10: {8: 3, 9: 1}
            }, 1, 10)
        ]

# find shortest path using bfs
for (graph, start, goal) in graphs:
    shortest_path = Pathfinding.bfs(graph, start, goal)
    print(shortest_path)


    