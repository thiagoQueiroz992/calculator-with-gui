from tkinter import *

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


class Application(Tk):
    def __init__(self):
        super().__init__()

        self.buttons = []

        self.display_frame = Frame(self, bg='#999999', width=400, height=75)
        self.numeric_keys_frame = Frame(self, bg="#FCFF67", width=200, height=250)
        self.operation_keys_frame = Frame(self, bg="#00E6BF", width=200, height=250)

        self.numeric_keys_frame.columnconfigure(0, minsize=66)
        self.numeric_keys_frame.columnconfigure(1, minsize=66)
        self.numeric_keys_frame.columnconfigure(2, minsize=66)

        self.operation_keys_frame.columnconfigure(0, minsize=66)
        self.operation_keys_frame.columnconfigure(1, minsize=66)
        self.operation_keys_frame.columnconfigure(2, minsize=66)

        self.display_frame.pack()
        self.numeric_keys_frame.pack(side='left')
        self.operation_keys_frame.pack(side='right')

        self.numeric_buttons_organization()
    
    def numeric_buttons_organization(self):
        keygrid = [3, 0]

        for b in range(-2, 10):
            if b == -2:
                self.buttons.append(Button(self.numeric_keys_frame, text='+/-', width=6, height=3, padx=4, pady=4))
                self.buttons[-1].grid(row=keygrid[0], column=keygrid[1])
            elif b == -1:
                self.buttons.append(Button(self.numeric_keys_frame, text='0', width=6, height=3, padx=4, pady=4))
                self.buttons[-1].grid(row=keygrid[0], column=keygrid[1])
            elif b == 0:
                self.buttons.append(Button(self.numeric_keys_frame, text=',', width=6, height=3, padx=4, pady=4))
                self.buttons[-1].grid(row=keygrid[0], column=keygrid[1])
            else:
                self.buttons.append(Button(self.numeric_keys_frame, text=str(b), width=6, height=3, padx=4, pady=4))
                self.buttons[-1].grid(row=keygrid[0], column=keygrid[1])

            if keygrid[1] == 2:
                keygrid[0] -= 1
                keygrid[1] = 0
            else:
                keygrid[1] += 1


test = Application()
test.mainloop()
