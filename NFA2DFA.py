import Queue

class NFA:
    def __init__(self, initial, final, states, transitions):
        self.initial = initial
        self.states = states
        self.final = final
        self.transitions = transitions

    def arrange(self, state):
        temp = []
        for i in range(1, len(state)):
            temp.append(int(state[i]))
        temp.sort()
        tempStr = [str(i) for i in temp]
        s = list(state)
        s[1:] = tempStr
        s = ''.join(s)
        return s

    def convert(self, q, DFAtrans, visited):
        if q.is_empty() :
            return DFAtrans

        current = q.dequeue()
        visited.append(current)

        DFAtrans[current] = []

        nextStates = []

        if current in self.transitions: nextStates = self.transitions[current]

        else:
            nStates = []
            for i in range(1,len(current)):
                tempState = 'q'+ current[i]
                nState = self.transitions[tempState]
                nStates.append(nState)
            nextStates = [list(e) for e in zip(*nStates)]

        for nextState in nextStates:
            if type(nextState)==list:
                newState = 'q'
                vis = []
                for s in nextState:
                    if s == '': continue
                    if type(s) == list:
                        for a in s:
                            if a[1] not in vis:
                                newState = newState + a[1]
                                vis.append(a[1])
                    elif s[1] not in vis:
                        newState = newState + s[1]
                        vis.append(s[1])
                newState = self.arrange(newState)
                DFAtrans[current].append(newState)

                if newState not in visited and newState != '': q.enqueue(newState)

            else:
                nextState = self.arrange(nextState)
                DFAtrans[current].append(nextState)
                if nextState not in visited and nextState != '': q.enqueue(nextState)
        return self.convert(q, DFAtrans, visited)






def main():
    I0 = {'q1':'q2', 'q2':['q1','q2']}
    I1 = {'q1' : 'q2', 'q2':'q4', 'q3':['q4','q5']}
    transitions = {'q1' : ['q2', 'q2'], 'q2': [['q1', 'q2'], 'q4'], 'q3':['q4', 'q5'], 'q4': ['q5', 'q2'], 'q5':['', '']}
    finalState = 'q5'
    initialState = 'q1'
    states = ['q1', 'q2', 'q3', 'q4', 'q5']
    # transitions = {}
    # transitions['I0'] = I0
    # transitions['I1'] = I1
    print('\n', '------------------NFA------------------------', '\n')
    print(transitions, '\n')

    nfa = NFA(initialState, finalState, states, transitions)
    q = Queue.Queue()
    q.enqueue(initialState)
    DFAtrans = {}
    visited = []
    print('Converting.....', '\n')
    dfa = nfa.convert(q, DFAtrans, visited)
    print('\n', '------------------DFA------------------------', '\n')
    print(dfa)


if __name__ == '__main__':
    main()
