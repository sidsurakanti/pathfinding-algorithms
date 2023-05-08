from pathfinding import Pathfinding

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
