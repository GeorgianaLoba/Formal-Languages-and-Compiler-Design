from src.FiniteAutomata import FiniteAutomata


def display():
    print('HEllO')
    print('Press 1 for displaying the set of states')
    print('Press 2 for displaying alphabet')
    print('Press 3 for initial state')
    print('Press 4 for set of final states')
    print('Press 5 for transitions')
    print('Press 6 for entire FA')
    print('Press 7 for checking if DFA')
    print('Press 8 for checking if your sequence is accepted by the FA')
    print('Press 0 for BYE! :)')


def main():
    fa = FiniteAutomata()
    fa.read_file('fa.in')
    while True:
        display()
        inp = int(input())
        if inp == 0:
            break
        if inp == 1:
            print("States: " + str(fa.Q) + "\n")
        if inp == 2:
            print("Alphabet: " + str(fa.Sigma) + "\n")
        if inp == 3:
            print("Initial state: " + str(fa.q0) + "\n")
        if inp == 4:
            print("Set of final states: " + str(fa.F) + "\n")
        if inp == 5:
            print('Transitions: \n')
            for transition in fa.Delta:
                print(transition)
        if inp == 6:
            print(fa)
        if inp == 7:
            result = fa.is_deterministic()
            if result:
                print('Is deterministic!')
            else:
                print('Not deterministic!')
        if inp == 8:

            sequence = input('\nEnter sequence: ')
            result = fa.is_accepted(sequence)
            if result:
                print(sequence + ' is accepted!')
            else:
                print(sequence + ' is not accepted!')


if __name__ == '__main__':
    main()
