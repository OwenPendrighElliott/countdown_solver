import sys
from collections import deque
from itertools import permutations

class numbers_game():
    def __init__(self, goal, nums, shortest=False):
        self.goal = goal
        self.nums = nums
        self.ops = [self.add, self.subtract, self.multiply, self.divide]
        self.shortest = shortest

    def add(self, a,b):
        return a+b
    
    def subtract(self, a,b):
        return a-b
    
    def multiply(self, a,b):
        return a*b
    
    # div can not return negative or float numbers
    def divide(self, a,b):
        if a == 0 or b == 0 or b>a:
            return 0 
        if a%b != 0:
            return 0
        return int(a/b)
    
    def solve(self):
        # initialise a deque for tracking progress
        Q = deque()
        Q.append((self.nums, []))
        nodes = 0
        while Q:
            ns, path = Q.pop()
            if self.goal in ns:
                print(f"Solution found after expanding {nodes} nodes")
                return path
            if len(ns) <= 1:
                continue
            for a, b in permutations(ns, 2):
                for op in self.ops:
                    nodes += 1
                    # calulate new value 
                    new_n = op(a, b)
                    # if value is negative then we dont need it
                    if new_n < 0:
                        continue

                    # create new list of numbers and new path
                    new_ns = list(ns)
                    new_ns.remove(a)
                    new_ns.remove(b)
                    new_ns.append(new_n)
                    new_path = list(path)
                    new_path.append((a, op.__name__, b, new_n))
                    # if shortest use LIFO (BFS)
                    if self.shortest:
                        Q.appendleft((new_ns, new_path))
                    # else use FIFO (DFS)
                    else:
                        Q.append((new_ns, new_path))
        raise Exception("No Solution available!")


def main():
    ns_str = sys.argv[1]
    nums = [int(n) for n in ns_str.split('-')]
    goal = int(sys.argv[2])
    if len(sys.argv)>3:
    	strat = bool(sys.argv[3])
    else:
    	strat = False
    game = numbers_game(goal, nums, strat)
    sol = game.solve()
    
    for a, op, b, r in sol:
        print(f"{op.capitalize()} {a} and {b} to get {r}")
        
if __name__ == '__main__':
    main()

