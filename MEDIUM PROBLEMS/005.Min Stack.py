class MinStack(object):

    def __init__(self):
        self.stack=[]     
        self.min_stack=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value,self.min_stack[-1]))    
          

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        
