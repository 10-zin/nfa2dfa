class NFA:
    def __init__(self, initial, final, states, transitions):
        self.initial = initial
        self.states = states
        self.final = final
        self.transitions = transitions

    def make():
        DFAtrans = {}
        stack = []
        stack.append(self.initial)

        current = stack.pop(len(stack)-1)

        if isinstance(current, list):
            listVal = []
            for curr in current:

                if curr in self.transitions:

                    value = self.transitions.get(current)
                    if isinstance(value, list):
                        listVal.append(value)
                        DFAtrans[current] = value

            if listVal is not i stack:
                stack.append(listVal)








        if current in self.transitions:
            value = self.transitions.get(current)
            if isinstance(value, list):
                stack.append(value)
                DFAtrans[current] = value




        # for trans in transitions:
        #     input = []
        #     for state in trans:
        #         for key in state:
        #             value = state.get(key)
        #             if isinstance(value, list):
        #                 for st in list:
        #                     stack.append(st)
        #
        #
        #             else:
        #                 stack.append(value)
        #                 input.append({key, value})







def main():
    I0 = {'q1':'q2', 'q2':['q1','q2']}
    I1 = {'q1' : 'q2', 'q2':'q4', 'q3':['q4','q5']}
    finalState = 'q5'
    initialState = 'q1'
    states = ['q1', 'q2', 'q3', 'q4', 'q5']
    transitions = []
    transitions.append(I0)
    transitions.append(I1)

    print transitions

    NFA(initialState, finalState, states, transitions)


if __name__ == 'main':
    main()
