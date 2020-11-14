

class IntcodeComputer:
    def __init__(self, ):
        pass

    def _add(self, instruction_pointer):
        x = memory[memory[instruction_pointer+1]]
        y = memory[memory[instruction_pointer+2]]
        memory[memory[instruction_pointer+3]] = x + y

    def _multiply(memory, instruction_pointer):
        x = memory[memory[instruction_pointer+1]]
        y = memory[memory[instruction_pointer+2]]
        memory[memory[instruction_pointer+3]] = x * y
