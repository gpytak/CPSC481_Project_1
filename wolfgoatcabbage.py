from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial, goal={}):
        super().__init__(initial, goal)

    

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        "possible actions should be Farmer, Farmer and Cabbage, Farmer and Goat, Farmer and Wolf cross the river"

        pass

    
    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        pass

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal


def main():
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

if __name__ == '__main__':
    main()
