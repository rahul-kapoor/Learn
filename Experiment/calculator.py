class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Function for addition1
    def addition(self):
        return self.a+self.b

    # Function for subtraction
    def subtract(self):
        return self.a-self.b

    # Function for multiplication
    def multiply(self):
        return self.a*self.b

    # Function for division
    def divide(self):
        if self.b == 0:
            raise ValueError('Can not divide by zero !')
        return self.a/self.b

