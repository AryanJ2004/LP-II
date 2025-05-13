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




#SECOND PROGRAM


class Node:
    def __init__(self, data, level, fval=0, parent=None):
        self.data, self.level, self.fval, self.parent = data, level, fval, parent

    def generate_child(self):
        x, y = next((i, j) for i in range(len(self.data)) for j in range(len(self.data[i])) if self.data[i][j] == '_')
        moves = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        children = []
        for nx, ny in moves:
            if 0 <= nx < len(self.data) and 0 <= ny < len(self.data[0]):
                new_data = [row[:] for row in self.data]
                new_data[x][y], new_data[nx][ny] = new_data[nx][ny], new_data[x][y]
                children.append(Node(new_data, self.level+1, parent=self))
        return children

class Puzzle:
    def __init__(self, n):
        self.n, self.open, self.closed = n, [], []

    def input_state(self, prompt):
        print(prompt)
        return [input(f"Row {i+1}: ").split() for i in range(self.n)]

    def h(self, state, goal):
        return sum(abs(i - x) + abs(j - y)
                   for i in range(self.n) for j in range(self.n)
                   if state[i][j] != '_' and (x:=next((a for a in range(self.n) for b in range(self.n) if goal[a][b]==state[i][j])), 
                                              y:=next((b for a in range(self.n) for b in range(self.n) if goal[a][b]==state[i][j]))))

    def f(self, node, goal):
        return self.h(node.data, goal) + node.level

    def solve(self, start, goal):
        start_node = Node(start, 0)
        start_node.fval = self.f(start_node, goal)
        self.open.append(start_node)
        visited = {str(start): start_node}

        while self.open:
            current = self.open.pop(0)
            if self.h(current.data, goal) == 0:
                self.print_solution(current)
                return
            for child in current.generate_child():
                child.fval = self.f(child, goal)
                if (s := str(child.data)) not in visited or visited[s].fval > child.fval:
                    self.open.append(child)
                    visited[s] = child
            self.open.sort(key=lambda x: x.fval)

    def print_solution(self, node):
        path = []
        while node:
            path.append(node)
            node = node.parent
        for i, n in enumerate(reversed(path)):
            print(f"\nStep {i}:")
            for row in n.data:
                print(' '.join(row))

def main():
    n = int(input("Enter puzzle size: "))
    p = Puzzle(n)
    start = p.input_state("Start State:")
    goal = p.input_state("Goal State:")
    p.solve(start, goal)

if __name__ == "__main__":
    main()
