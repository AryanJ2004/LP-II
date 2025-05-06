class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        x, y = self.find('_')
        moves = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        children = []
        for nx, ny in moves:
            if 0 <= nx < len(self.data) and 0 <= ny < len(self.data):
                new_data = [row[:] for row in self.data]
                new_data[x][y], new_data[nx][ny] = new_data[nx][ny], new_data[x][y]
                children.append(Node(new_data, self.level + 1, 0))
        return children

    def find(self, val):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == val:
                    return i, j

class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        return [input().split() for _ in range(self.n)]

    def f(self, node, goal):
        return self.h(node.data, goal) + node.level

    def h(self, start, goal):
        return sum(start[i][j] != goal[i][j] and start[i][j] != '_' for i in range(self.n) for j in range(self.n))

    def process(self):
        print("Enter start state:")
        start = self.accept()
        print("Enter goal state:")
        goal = self.accept()
        start_node = Node(start, 0, self.f(Node(start, 0, 0), goal))
        self.open.append(start_node)   
        step = 0
        while self.open:
            cur = self.open.pop(0)
            print(f"Step {step}:")
            for row in cur.data:
                print(" ".join(row))
            print()
            if self.h(cur.data, goal) == 0:
                break  
            self.closed.append(cur)
            for child in cur.generate_child():
                child.fval = self.f(child, goal)
                self.open.append(child)
            self.open.sort(key=lambda x: x.fval)   
            print("↓" * 5 + "\n")  # Downward arrows
            step += 1


# Run
Puzzle(3).process()
