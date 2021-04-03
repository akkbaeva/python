class Stack:

    def __init__(self, array):
        self.array = array



    def add(self, element):
        self.array.append(element)

    def remote(self):
        self.array.pop()

    def __str__(self):
        return f'{self.array}'

stack = Stack([])
stack.add("p")
stack.add("y")
stack.add("t")
stack.add("h")
stack.add("o")
stack.add("n")
stack.add("p")
print(stack)
stack.remote()
stack.remote()
print(stack)
stack.add("n")
print(stack)

