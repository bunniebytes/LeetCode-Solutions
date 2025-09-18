class MyQueue(object):
    def __init__(self):
        self.first_item = None
        self.input_stack = []
        self.output_stack = []
        

    def push(self, x):
        if self.empty():
            self.first_item = x
        if len(self.output_stack) > 0:
            self.switch_stacks(self.output_stack, self.input_stack)
        self.input_stack.append(x)
        

    def pop(self):
        popped_item = None
        if len(self.input_stack) > 0:
            self.switch_stacks(self.input_stack, self.output_stack)
        if len(self.output_stack) > 0:
            popped_item = self.output_stack.pop()
        if len(self.output_stack) == 0:
            self.first_item = None
        else:
            self.first_item = self.output_stack[-1]
        return popped_item

    def peek(self):
       return self.first_item

    def empty(self):
        if len(self.input_stack) == 0 and len(self.output_stack) == 0:
            return True
        return False
    
    def switch_stacks(self, not_empty, empty):
        while len(not_empty) > 0:
            empty.append(not_empty.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()