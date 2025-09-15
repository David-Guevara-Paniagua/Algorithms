class Stack():
    stack=[]
    def isEmpty(self)->bool:
        if len(self.stack)==0: return True
        return False
    def pop(self):
        if not self.isEmpty(): return self.stack.pop()
        return None
    def push(self,value):
        self.stack.append(value)
    def __str__(self):
        return "Pila: "+str(self.stack)
    def __len__(self):
        return len(self.stack)

