# INF1340 Midterm Project
# Amy Li
# NP-Puzzle chosen: n-puzzle 3x3

# Modified from Ajinkya Sonawane's implentation of n-puzzle in python 
# https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288
# Changed the goal state user input to a fixed goal state by user

class Node:
    def __init__(self,hvalue,gvalue,fvalue):
        # Initialize the node with the hvalue, gvalue of the node and the calculated fvalue, part of the A* algorithmn used to solve the n-puzzle. 
        self.hvalue = hvalue
        self.gvalue = gvalue
        self.fvalue = fvalue

    def child(self):
        # Generate child nodes from the given node by moving the blank space either in the 4 possible directions of [up,down,left,right]. The move_blank contains position values for moving the blank space in either of the 4 directions.
        x,y = self.find(self.hvalue,'-')
        move_blank = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in move_blank:
            child = self.shuffle(self.hvalue,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.gvalue+1,'-')
                children.append(child_node)
        return children
        
    def shuffle(self,puz,x1,y1,x2,y2):
        # Move the blank space in the given direction. The n-puzzle has boundaries, so sometimes the position to move to is not available. If the position value are out of limits the return None.
        if x2 >= 0 and x2 < len(self.hvalue) and y2 >= 0 and y2 < len(self.hvalue):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
            

    def copy(self,start_state):
        # Copy function to create a similar matrix of the given puzzle start state.
        temp = []
        for i in start_state:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self,puz,x):
        # Used to find the position of the blank space of the given puzzle start state.
        for i in range(0,len(self.hvalue)):
            for j in range(0,len(self.hvalue)):
                if puz[i][j] == x:
                    return i,j


class Puzzle:
    def __init__(self,size):
        # Initialize the puzzle size by the specified size, open and closed lists to empty
        self.n = size
        self.open = []
        self.closed = []

    def accept_start_state(self):
        # Accepts the start state puzzle from the user
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def goal_state(self):
        # Defines the goal state puzzle
        puz = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '-']]
        return puz

    def f(self,start,goal):
       # A* Algorithm to calculate hueristic value f(x) = h(x) + g(x)
        return self.h(start.hvalue,goal)+start.gvalue

    def h(self,start,goal):
        # Calculates the differences between the given state state and the defined goal state
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '-':
                    temp += 1
        return temp

    def process(self):
        # Asks user to input a start state puzzle plus instructions. Prints goal state puzzle.
        print("Hello, here is a solver for a 3 x 3 sliding n-puzzle :)")
        print("Enter the start state 3 by 3 matrix with numbers ranging from 1 to 8.\n" "Input '-' to represent the blank space.\n" "Put a space between each input. Press the 'enter' key after each row of three inputs.\n" "For example:\n"'1', '2', '3\n''-', '4', '6\n' '7', '5', '8\n')
        start = self.accept_start_state()
        print("Goal state of matrix is\n" '1', '2', '3\n''4', '5', '6\n' '7', '8', '-') 
        goal = self.goal_state()
        
        start = Node(start,0,0)
        start.fvalue = self.f(start,goal)
        # Puts the start state puzzle in the open node
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("...next")
            for i in cur.hvalue:
                for j in i:
                    print(j,end=" ")
                print("")
            # The goal state is reached when h(n) = 0 or there is not difference between the start state and the finish state.
            if(self.h(cur.hvalue,goal) == 0):
                break
            for i in cur.child():
                i.fvalue = self.f(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            # Sorts the open list based on the fvalue
            self.open.sort(key = lambda x:x.fvalue,reverse=False)

# Defines puzzle as a 3x3 puzzle to solve
puz = Puzzle(3)
puz.process()
print("Done!")