from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial={('F', 'W', 'G', 'C')}, goal=(frozenset())):
        super().__init__(initial, goal)
    
    def goal_test(self, state):
        """ Given a state, return True if state is a goal state, or False otherwise """
        # print()
        # print("Goal: ", self.goal)
        # print("State: ", state)
        # print()
        return state == self.goal

    def result(self, state, action):
        # returns the new state reached from the given state and the given action. Assume that the action is valid.
            # In result() you will have to return the next state as a frozenset since the search algorithms
            # require the state to be represented as a hashable data type.
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        new_state = state
        left_bank = ()

        print("State: ", tuple(state))
        print("Action: ", list(action))

        # Moving Farmer and Goat from Left Bank
        if tuple(state) == ('F', 'W', 'G', 'C') and list(action) == ['F', 'G']:  # {'F', 'G')
            left_bank = ('W', 'C')
        if tuple(state) == ('W', 'C') or tuple(state) == ('C', 'W') and list(action) == ['F']:   # ('F')
            left_bank = ('W', 'C')
        
        # Taking Wolf or Cabbage from Left bank  ('F', 'W'), or ('F', 'C')
        if tuple(state) == ('W', 'C') or tuple(state) == ('C', 'W') and list(action) == ['F', 'W']: 
            left_bank = ('C',)
        if tuple(state) == ('W', 'C') or tuple(state) == ('C', 'W') and list(action) == ['F', 'C']:
            left_bank = ('W',)

        # Taking Wolf from Left bank  # ('F', 'G') or ('F', 'W')
        if tuple(state) == ('W',) and list(action) == ['F', 'G']:
            left_bank = ('W',)
        if tuple(state) == ('W',) and list(action) == ['F', 'W']:
            left_bank = ('G',)

        # Taking Cabbage from Left bank  # ('F', 'G') or ('F', 'C')
        if tuple(state) == ('C',) and list(action) == ['F', 'G']:
            left_bank = ('C',)
        if tuple(state) == ('C',) and list(action) == ['F', 'C']:
            left_bank = ('G',)

        # Taking Goat from Left bank # ('F') or ('F', 'G')
        if tuple(state) == ('G',) and list(action) == ['F']:
            left_bank = ('G',)
        if tuple(state) == ('G',) and list(action) == ['F', 'G']:
            left_bank = ()

        print("left_bank: ", left_bank)
        print()
        new_state = frozenset(left_bank)
        return new_state

# State = Left Bank
# Action = Boat Crossing

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = [['F'], ['F', 'W'], ['F', 'G'], ['F', 'C']]

        if tuple(state) == ('F', 'W', 'G', 'C'): # {'F', 'G'}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if tuple(state) == ('W', 'C') or tuple(state) == ('C', 'W'):  # {'F'}, {'F', 'W'}, or {'F', 'C'}
            del possible_actions[2]
        if tuple(state) == ('W',): # {'F', 'G'} or {'F', 'W'}
            del possible_actions[3]
            del possible_actions[0]
        if tuple(state) == ('C',): # {'F', 'G'} or {'F', 'C'}
            del possible_actions[1]
            del possible_actions[0]
        if tuple(state) == ('G',): # {'F'} or {'F', 'G'}
            del possible_actions[3]
            del possible_actions[1]
        if tuple(state) == ():
            del possible_actions[3]
            del possible_actions[2]
            del possible_actions[1]
            del possible_actions[0]

        print("State: ", tuple(state))
        print("possible_actions: ", possible_actions)
        print()

        return possible_actions

def main():
    wgc = WolfGoatCabbage(('F', 'W', 'G', 'C')) # Needs 'initial' passed in
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

if __name__ == '__main__':
    main()
