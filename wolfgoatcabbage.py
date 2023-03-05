from search import *


class WolfGoatCabbage(Problem):

    def __init__(self, initial={("F", "W", "G", "C")}, goal=(frozenset())):
        super().__init__(initial, goal)
    
    def goal_test(self, state):
        """ Given a state, return True if state is a goal state, or False otherwise """

        return state == self.goal

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        new_state = state
        left_bank = {}

        # Moving Farmer and Goat from Left Bank
        if set(state) == {"F", "W", "G", "C"} and action == {"F", "G"}:  # {"F", "G")
            left_bank = {"W", "C"}
        
        # Taking Wolf or Cabbage from Left bank  # ("F"), ("F", "W"), or ("F", "C")
        if set(state) == {"W", "C"} and action == {"F"}:
            left_bank = {"F", "W", "C"}
        if set(state) == {"F", "W", "C"} and action == {"F", "W"}:
            left_bank = ("C",)
        if set(state) == {"F", "W", "C"} and action == {"F", "C"}:
            left_bank = {"W",}

        # Taking Wolf from Left bank  # ("F", "G") or ("F", "W")
        if set(state) == {"W",} and action == {"F", "G"}:
            left_bank = {"F", "W", "G"}
        if set(state) == {"F", "W", "G"} and action == {"F", "W"}:
            left_bank = {"G",}

        # Taking Cabbage from Left bank  # ("F", "G") or ("F", "C")
        if set(state) == {"C",} and action == {"F", "G"}:
            left_bank = {"F", "G", "C"}
        if set(state) == {"F", "G", "C"} and action == {"F", "C"}:
            left_bank = {"G",}

        # Taking Goat from Left bank # ("F") or ("F", "G")
        if set(state) == {"G",} and action == {"F"}:
            left_bank = {"F", "G"}
        if set(state) == {"F", "G"} and action == {"F", "G"}:
            left_bank = {}

        new_state = frozenset(left_bank)
        return new_state

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = [{"F"}, {"F", "W"}, {"F", "G"}, {"F", "C"}]

        if set(state) == {"F", "W", "G", "C"}: # {"F", "G"}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if set(state) == {"W", "C"}:  # {"F"}
            del possible_actions[3]
            del possible_actions[2]
            del possible_actions[1]
        if set(state) == {"F", "W", "C"}: # {"F", "W"} or {"F", "C"}
            del possible_actions[2]
            del possible_actions[0]
        if set(state) == {"W",}: # {"F", "G"}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if set(state) == {"F", "W", "G"}: # {"F", "W"}
            del possible_actions[3]
            del possible_actions[2]
            del possible_actions[0]
        if set(state) == {"C",}: # {"F", "G"}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if set(state) == {"F", "G", "C"}: # {"F", "C"}
            del possible_actions[2]
            del possible_actions[1]
            del possible_actions[0]
        if set(state) == {"G",}: # {"F"}
            del possible_actions[3]
            del possible_actions[2]
            del possible_actions[1]
        if set(state) == {"F", "G"}: # {"F", "G"}
            del possible_actions[3]
            del possible_actions[1]
            del possible_actions[0]
        if set(state) == {}:
            del possible_actions[3]
            del possible_actions[2]
            del possible_actions[1]
            del possible_actions[0]

        return possible_actions

def main():
    wgc = WolfGoatCabbage(("F", "W", "G", "C"))
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

if __name__ == '__main__':
    main()
