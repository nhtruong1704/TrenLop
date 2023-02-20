from enum import Enum
class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
class StateMachine:
    state = State.A
    def show(self):
        return self.update({
            State.A: [State.B, 0],
            State.B: [State.F, 3],
            State.C: [State.D, 4],
            State.D: [State.E, 5],
            State.E: [State.F, 7],
        })
    def race(self):
        return self.update({
            State.B: [State.B, 2],
        })
    def cast(self):
        return self.update({
            State.B: [State.C, 1],
            State.D: [State.B, 6],
            State.F: [State.A, 8],
        })
    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal
def main():
    return StateMachine()
print(o.show())

