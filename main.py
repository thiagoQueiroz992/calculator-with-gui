class Calculator:
    def __init__(self):
        self.operators = {
            0: 'Summing',
            1: 'Subtraction',
            2: 'Multiplication',
            3: 'Division'
        }
    
    def sum(self, a: float, b: float) -> float:
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiplicate(self, a: float, b: float) -> float:
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        return a / b
