

class IntcodeComputer:
    def __init__(self, memory_array):
        self.memory_array = memory_array

    def compute(self):
        for i in range(0, len(memory_array), 4):
            operator = memory_array[i]
            if operator == 99:
                break
            if operator == 1:
                _add(memory_array, i)
                continue
            if operator == 2:
                _multiply(memory_array, i)
                continue
            raise ValueError(f'Unexpected operator: {memory_array[i]}')
        return memory_array[0]

    def _add(self, instruction_pointer):
        x = memory[memory[instruction_pointer+1]]
        y = memory[memory[instruction_pointer+2]]
        memory[memory[instruction_pointer+3]] = x + y

    def _multiply(memory, instruction_pointer):
        x = memory[memory[instruction_pointer+1]]
        y = memory[memory[instruction_pointer+2]]
        memory[memory[instruction_pointer+3]] = x * y
