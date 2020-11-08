import time
import move as m
import operator
import tf_image_detection as tf

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def adder(start, next):
    ''' Updates the location of the vehicle '''
    return tuple(map(operator.add, next, start))

def update_map(maze, start, direction):
    x, y = start
    if direction == "east":
        x = x + 1
    elif direction == "south":
        y = y + 1
    elif direction == "west":
        x = x - 1
    #if scan():
    #    maze[x][y] = 1
    return maze

def main():

    maze = [[0, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 0]]

    start = (0, 0)
    end = (4, 0)
    direction = "east"

    move_count = 0
    path = astar(maze, start, end)
    print("Calculating A-Star Algorithm")
    print(path)

    while (start != end):
        if tf.can_move():
            path = astar(maze, start, end)
            next = (path[1][0] - start[0], path[1][1] - start[1])
            if direction == "east":
                if next == (0, 1):
                    m.mforward()
                    start = adder(start, next)
                elif next == (1, 0):
                    m.mright()
                    m.mforward()
                    direction = "south"
                    start = adder(start, next)
                elif next == (0, -1):
                    m.mright()
                    m.mright()
                    m.mforward()
                    direction = "west"
                    start = adder(start, next)
                print("Next move is " + str(next))
                print("Current location is" + str(start) + " and direction is " + direction)
                print("Move count is: " + str(move_count))
                move_count += 1

                update_map(maze, start, direction)
            elif direction == "south":
                if next == (0, 1):
                    m.mleft()
                    m.mforward()
                    direction = "east"
                    start = adder(start, next)
                elif next == (1, 0):
                    m.mforward()
                    start = adder(start, next)
                elif next == (0, -1):
                    m.mright()
                    m.mforward()
                    direction = "west"
                    start = adder(start, next)
                print("Next move is " + str(next))
                print("Current location is" + str(start) + " and direction is " + direction)
                print("Move count is: " + str(move_count))
                move_count += 1

                update_map(maze, start, direction)
            elif direction == "west":
                if next == (0, 1):
                    m.mright()
                    m.mright()
                    m.mforward()
                    direction = "east"
                    start = adder(start, next)
                elif next == (1, 0):
                    m.mleft()
                    m.mforward()
                    direction = "south"
                    start = adder(start, next)
                elif next == (0, -1):
                    m.mforward()
                    start = adder(start, next)
                print("Next move is " + str(next))
                print("Current location is" + str(start) + " and direction is " + direction)
                print("Move count is: " + str(move_count))
                move_count += 1

                update_map(maze, start, direction)
        else:
            time.sleep(5)

    #navigate(path, facing)


if __name__ == '__main__':
    main()

