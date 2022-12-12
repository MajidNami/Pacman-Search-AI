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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # define a stack for open list
    open_stack = util.Stack()
    # initialize open stack with start position
    open_stack.push((problem.getStartState(),'start',0))
    # define a stack for closed list
    closed_stack = util.Stack()
    backtrack_checkpoints = util.Stack()
    visited_list = []

    while not open_stack.isEmpty():

        A = open_stack.pop()
        visited_list.append(A[0])
        if problem.isGoalState(A[0]):
            closed_stack.push(A)
            break
        else:
            # generate successors of A
            children_of_A = problem.getSuccessors(A[0])
            # push A on closed stack
            closed_stack.push(A)
            alreadyVisitedChildren = 0
            for each_child in children_of_A:
                if (each_child[0] in visited_list):
                    alreadyVisitedChildren +=1
                else:
                    open_stack.push(each_child)

            if (len(children_of_A) - alreadyVisitedChildren) > 1:
                backtrack_checkpoints.push(A)
                if len(children_of_A) == 4:
                    backtrack_checkpoints.push(A)

            if alreadyVisitedChildren == len(children_of_A):
                return_point = backtrack_checkpoints.pop()
                temp_point = closed_stack.pop()
                while return_point[0] != temp_point[0]:
                    temp_point = closed_stack.pop()
                closed_stack.push(temp_point)
    actions = []
    while not closed_stack.isEmpty():
        dir = closed_stack.pop()[1]
        if dir!='start':
                actions.append(dir)

    actions.reverse()
    return actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # define a queue for open list
    open_queue = util.Queue()
    # initialize open stack with start position
    open_queue.push((problem.getStartState(), []))
    visited_list = []

    while not open_queue.isEmpty():
        A, actions = open_queue.pop()
        if A not in visited_list:
            visited_list.append(A)
            if problem.isGoalState(A):
                return actions
            else:
                # generate successors of A
                    children_of_A = problem.getSuccessors(A)

                    for each_child in children_of_A:
                            open_queue.push((each_child[0], actions + [each_child[1]]))
    return []



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
