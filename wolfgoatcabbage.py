# Gregory Pytak and Nolan Winter
# CPSC 481 Project 1

from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial=(frozenset(("F", "W", "G", "C"))), goal=(frozenset())):
        super().__init__(initial, goal)
    
    def goal_test(self, state):
        """ Given a state, return True if state is a goal state, or False otherwise """

        return state == self.goal

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        new_state = {}

        # Moving Farmer and Goat from Left Bank
        if frozenset(frozenset(set(state))) == frozenset({"F", "W", "G", "C"}) and action == {"F", "G"}:  # ("F", "G")
            new_state = {"W", "C"}
        
        # Taking Wolf or Cabbage from Left bank  # ("F"), ("F", "W"), or ("F", "C")
        if frozenset(set(state)) == frozenset({"W", "C"}) and action == {"F"}:
            new_state = frozenset({"F", "W", "C"})
        if frozenset(set(state)) == frozenset({"F", "W", "C"}) and action == frozenset({"F", "W"}):
            new_state = {"C",}
        if frozenset(set(state)) == frozenset({"F", "W", "C"}) and action == frozenset({"F", "C"}):
            new_state = {"W",}

        # Taking Wolf from Left bank  # ("F", "G") or ("F", "W")
        if frozenset(set(state)) == frozenset({"W",}) and action == {"F", "G"}:
            new_state = {"F", "W", "G"}
        if frozenset(set(state)) == frozenset({"F", "W", "G"}) and action == {"F", "W"}:
            new_state = {"G",}

        # Taking Cabbage from Left bank  # ("F", "G") or ("F", "C")
        if frozenset(set(state)) == frozenset({"C",}) and action == {"F", "G"}:
            new_state = {"F", "G", "C"}
        if frozenset(set(state)) == frozenset({"F", "G", "C"}) and action == {"F", "C"}:
            new_state = {"G",}

        # Taking Goat from Left bank # ("F") or ("F", "G")
        if frozenset(set(state)) == frozenset({"G",}) and action == {"F"}:
            new_state = {"F", "G"}
        if frozenset(set(state)) == frozenset({"F", "G"}) and action == {"F", "G"}:
            new_state = {}
        
        return frozenset(new_state)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = [{"F"}, {"F", "W"}, {"F", "G"}, {"F", "C"}]

        if frozenset(set(state)) == {"F", "W", "G", "C"}: # {"F", "G"}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if frozenset(set(state)) == {"W", "C"}:  # {"F"}
            del possible_actions[3]
            del possible_actions[2]
            del possible_actions[1]
        if frozenset(set(state)) == frozenset({"F", "W", "C"}): # {"F", "W"} or {"F", "C"}
            del possible_actions[2]
            del possible_actions[0]
        if frozenset(set(state)) == frozenset({"W",}): # {"F", "G"}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if frozenset(set(state)) == {"F", "W", "G"}: # {"F", "W"}
            del possible_actions[3]
            del possible_actions[2]
            del possible_actions[0]
        if frozenset(set(state)) == {"C",}: # {"F", "G"}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if frozenset(set(state)) == {"F", "G", "C"}: # {"F", "C"}
            del possible_actions[2]
            del possible_actions[1]
            del possible_actions[0]
        if frozenset(set(state)) == {"G",}: # {"F"}
            del possible_actions[3]
            del possible_actions[2]
            del possible_actions[1]
        if frozenset(set(state)) == {"F", "G"}: # {"F", "G"}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if frozenset(set(state)) == {}:
            del possible_actions[3]
            del possible_actions[2]
            del possible_actions[1]
            del possible_actions[0]
        
        return possible_actions

def main():
    wgc = WolfGoatCabbage(frozenset(("F", "W", "G", "C")))
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

if __name__ == '__main__':
    main()
