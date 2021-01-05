# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    start = (problem.getStartState(), 'None', 0)
    traceMap = {}

    fringe = util.Stack()
    fringe.push(start)
    reached = []
    while not fringe.isEmpty() :
        curPlan = fringe.pop()
        if problem.isGoalState(curPlan[0]) :

            solution = util.Stack()
            curr = curPlan
            while curr != start :
                solution.push(curr[1])
                curr = traceMap[curr]

            actions = []
            while not solution.isEmpty() : 
                s = solution.pop()
                # if s != "None":
                actions.append(s);
            return actions

        if curPlan[0] in reached :
            continue
        reached.append(curPlan[0])

        potentialPlans = problem.getSuccessors(curPlan[0])
        for potentialPlan in potentialPlans :
            fringe.push(potentialPlan)
            traceMap[potentialPlan] = curPlan
    return []    

def genericSearch(problem, fringe, heuristic=None):
    """
    Generic search algorithm that takes a problem and a queuing strategy
    and performs a search given that strategy
    Written Answers for Question 1
    1. The exploration order is what I would have expected. The search goes as
       deep as it can, before exploring other paths (as would be expected with 
       depth first search).
    2. No, Pacman does not go to all of the explored squares on the way to the 
       goal. He follows a path that does not lead him to any dead-ends, even if
       dead ends were explored. In my implementation, the length for a 
       MediumMaze was 130.
    3. This is not the least-cost solution -- there is clearly a cheaper 
       solution that Pacman does not take on the MediumMaze. This is because
       DFS will return the first solution that it finds that solves the problem,
       not the best solution.
    Written Answers for Question 4
    1. With OpenMaze, BFS, UCS, and A* all find the shortest path to the goal, 
       with BFS and UCS expanding the same number of search nodes (682) and A*
       expanding the least amount of nodes (535). All paths have a cost of 54.
       DFS does find the solution as well, but is not the shortest -- the cost
       of the path found with DFS was 298. This is because DFS does not look 
       for the shortest path.
    """

    visited = []        # List of already visisted nodes
    action_list = []    # List of actions taken to get to the current node
    initial = problem.getStartState()   # Starting state of the problem

    # Push a tuple of the start state and blank action list onto the given
    # fringe data structure. If a priority queue is in use, then calculate
    # the priority using the heuristic
    if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
        fringe.push((initial, action_list))
    elif isinstance(fringe, util.PriorityQueue):
        fringe.push((initial, action_list), heuristic(initial, problem))

    # While there are still elements on the fringe, expand the value of each 
    # node for the node to explore, actions to get there, and the cost. If the
    # node isn't visited already, check to see if node is the goal. If no, then
    # add all of the node's successors onto the fringe (with relevant 
    # information about path and cost associated with that node)
    while fringe: 
        if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
            node, actions = fringe.pop() 
        elif isinstance(fringe, util.PriorityQueue):
            node, actions = fringe.pop()
        
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            successors = problem.getSuccessors(node)
            for successor in successors:
                coordinate, direction, cost = successor
                newActions = actions + [direction]
                if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
                    fringe.push((coordinate, newActions))
                elif isinstance(fringe, util.PriorityQueue):
                    newCost = problem.getCostOfActions(newActions) + \
                               heuristic(coordinate, problem)
                    fringe.push((coordinate, newActions), newCost)                  

    return []
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    fringe = util.Queue()
    fringe.push((problem.getStartState(), []))
    reached = []
    while not fringe.isEmpty() :
        state,actions  = fringe.pop()
        if problem.isGoalState(state) :
            print actions
            return actions

        if state in reached :
            continue
        reached.append(state)

        potentialPlans = problem.getSuccessors(state)
        for potentialPlan in potentialPlans :
            coordinate, direction, cost = potentialPlan
            newActions = actions + [direction]
            fringe.push((coordinate, newActions))
    return []

def uniformCostSearch(problem):
    start = (problem.getStartState(), 'None', 0)
    fringe = util.PriorityQueue()
    fringe.push(start, 0)

    traceMap = {}
    reached = []
    while not fringe.isEmpty() :
        item = fringe.popWithCost()
        curCost = item[0]
        curPlan = item[2]
        if problem.isGoalState(curPlan[0]) :
            solution = util.Stack()
            curr = curPlan
            while curr != start :
                solution.push(curr[1])
                curr = traceMap[curr]

            actions = []
            while not solution.isEmpty() : 
                s = solution.pop()
                # if s != "None":
                actions.append(s);
            return actions
        
        if curPlan[0] in reached :
            continue
        reached.append(curPlan[0])
        
        potentialPlans = problem.getSuccessors(curPlan[0])
        print potentialPlans
        for potentialPlan in potentialPlans :
            cost = curCost + potentialPlan[2]
            fringe.update(potentialPlan, cost)
            traceMap[potentialPlan] = curPlan
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), []), 0)
    reached = []
    while not fringe.isEmpty() :
        item = fringe.popWithCost()
        curCost = item[0]
        state,actions = item[2]
        if problem.isGoalState(state) :
            return actions

        if state in reached :
            continue
        reached.append(state)

        potentialPlans = problem.getSuccessors(state)
        for potentialPlan in potentialPlans :
            coordinate, direction, cost = potentialPlan
            h = heuristic(coordinate, problem)

            newActions = actions + [direction]
            fringe.update((coordinate, newActions), curCost + h + cost)
    return []


    # # util.raiseNotDefined()
    # start = (problem.getStartState(), 'None', 0)
    # fringe = util.PriorityQueue()
    # fringe.push(start, heuristic(start[0], problem))

    # traceMap = {}
    # reached = []
    # while not fringe.isEmpty() :
    #     item = fringe.popWithCost()
    #     curCost = item[0]
    #     curPlan = item[2]
    #     if problem.isGoalState(curPlan[0]) :
    #         solution = util.Stack()
    #         curr = curPlan
    #         while curr != start :
    #             solution.push(curr[1])
    #             curr = traceMap[curr]

    #         actions = []
    #         while not solution.isEmpty() : 
    #             s = solution.pop()
    #             # if s != "None":
    #             actions.append(s);
    #         return actions
        
    #     if curPlan[0] in reached :
    #         continue
    #     reached.append(curPlan[0])
        
    #     potentialPlans = problem.getSuccessors(curPlan[0])
    #     print potentialPlans
    #     for potentialPlan in potentialPlans :
    #         cost = curCost + potentialPlan[2]
    #         h = heuristic(potentialPlan[0], problem)
    #         fringe.update(potentialPlan, h + cost)
    #         traceMap[potentialPlan] = curPlan
    # return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
