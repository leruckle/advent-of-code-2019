class IntcodeComputer:
    def __init__(self):
        self.memory = []

    def run(self, program):
        self.memory = program
        for i in range(0, len(self.memory), 4):
            operator = self.memory[i]
            if operator == 99:
                break
            if operator == 1:
                self._add(self.memory, i)
                continue
            if operator == 2:
                self._multiply(self.memory, i)
                continue
            raise Exception(f'Unexpected operator: {self.memory[i]}')
        return self.memory[0]

    def _add(self, instruction_pointer):
        x = self.memory[self.memory[instruction_pointer+1]]
        y = self.memory[self.memory[instruction_pointer+2]]
        self.memory[self.memory[instruction_pointer+3]] = x + y

    def _multiply(self, instruction_pointer):
        x = self.memory[self.memory[instruction_pointer+1]]
        y = self.memory[self.memory[instruction_pointer+2]]
        self.memory[self.memory[instruction_pointer+3]] = x * y
