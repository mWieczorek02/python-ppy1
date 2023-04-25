class Node:
    def __init__(self, name, distance):
        self.name = name
        self.neighbours = []
        self.distance = distance
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbours.append(neighbor)

    def get_neighbors(self):
        return self.neighbours

    def get_distance(self):
        return self.distance

    def set_previous(self, previous):
        self.previous = previous


class Dijkstra:
    def get_distance(self, source: Node, name: str, distance=0):
        neighbours = source.get_neighbors()
        closest = None
        for neighbour in neighbours:
            if neighbour.visited == True:
                continue
            if neighbour.name == name:
                return distance + neighbour.distance
            neighbour.visited = True
            if closest == None:
                closest = neighbour
            elif closest.distance > neighbour.distance:
                closest = neighbour
        if closest == None:
            return distance
        else:
            distance += self.get_distance(closest,
                                          name, distance + closest.distance)
            return distance


def main():
    node = Node("1", 0)
    node2 = Node("4", 1)
    node2.add_neighbor(Node("10", 5))
    node.add_neighbor(Node("2", 4))
    node.add_neighbor(Node("3", 2))
    node.add_neighbor(node2)
    node.add_neighbor(Node("5", 3))
    node.add_neighbor(Node("6", 10))
    print(Dijkstra().get_distance(node, "10", 0))


if __name__ == "__main__":
    main()
