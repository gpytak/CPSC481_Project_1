from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial={'F','W','G','C'}, goal={}):
        super().__init__(initial, goal)
    
    def goal_test(self, state):
        """ Given a state, return True if state is a goal state, or False otherwise """
        
        return state == self.goal

    def result(self, state, action):
        # returns the new state reached from the given state and the given action. Assume that the action is valid.
            # In result() you will have to return the next state as a frozenset since the search algorithms
            # require the state to be represented as a hashable data type.
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        new_state = list(state)
        left_bank = []

        # Moving Farmer and Goat from Left Bank
        if state == {'F', 'W', 'G', 'C'}:  # {'F', 'G'}
            left_bank = ['W', 'C']
        if state == {'W', 'C'} and action == ['F']:   # {'F'}
            left_bank = ['W', 'C']
        
        # Taking Wolf or Cabbage from Left bank  {'F', 'W'}, or {'F', 'C'}
        if state == {'W', 'C'} and action == ['F', 'W']: 
            left_bank = ['C']
        if state == {'W', 'C'} and action == ['F', 'C']:
            left_bank = ['W']

        # Taking Wolf from Left bank  # {'F', 'G'} or {'F', 'W'}
        if state == {'W'} and action == ['F', 'G']:
            left_bank = ['W']
        if state == {'W'} and action == ['F', 'W']:
            left_bank = ['G']

        # Taking Cabbage from Left bank  # {'F', 'G'} or {'F', 'C'}
        if state == {'C'} and action == ['F', 'G']:
            left_bank = ['C']
        if state == {'C'} and action == ['F', 'C']:
            left_bank = ['G']

        # Taking Goat from Left bank # {'F'} or {'F', 'G'}
        if state == {'G'} and action == ['F']:
            left_bank = ['G']
        if state == {'G'} and action == ['F', 'G']:
            left_bank = []

        new_state = frozenset(left_bank)

        return new_state

# State = Left Bank
# Action = Boat Crossing

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = [['F'], ['F', 'W'], ['F', 'G'], ['F', 'C']]

        if state == {'F', 'W', 'G', 'C'}: # {'F', 'G'}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if state == {'W', 'C'}:  # {'F'}, {'F', 'W'}, or {'F', 'C'}
            del possible_actions[2]
        if state == {'W'}: # {'F', 'G'} or {'F', 'W'}
            del possible_actions[3]
            del possible_actions[0]
        if state == {'C'}: # {'F', 'G'} or {'F', 'C'}
            del possible_actions[1]
            del possible_actions[0]
        if state == {'G'}: # {'F'} or {'F', 'G'}
            del possible_actions[3]
            del possible_actions[1]

        return possible_actions

def main():
    wgc = WolfGoatCabbage(('F', 'W', 'G', 'C')) # Needs 'initial' passed in
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

if __name__ == '__main__':
    main()
