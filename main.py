from tkinter import *
from decimal import Decimal

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

        self.display = Label(self.display_frame, text='0', bg='#D4D4D4', relief='sunken', font=('TkDefaultFont', 30), width=16, anchor='e')

        self.display_frame.pack()
        self.numeric_keys_frame.pack(side='left')
        self.operation_keys_frame.pack(side='right')

        self.display.pack()

        self.numeric_buttons_organization()
    
    def numeric_buttons_organization(self):
        keygrid = [3, 0]

        for b in range(-2, 10):
            if b == -2:
                self.buttons.append(Button(self.numeric_keys_frame, text='+/-', width=6, height=3, padx=4, pady=4, command=lambda char=str(b): self.button_action(self.display, char)))
                self.buttons[-1].grid(row=keygrid[0], column=keygrid[1])
            elif b == -1:
                self.buttons.append(Button(self.numeric_keys_frame, text='0', width=6, height=3, padx=4, pady=4, command=lambda char='0': self.button_action(self.display, char)))
                self.buttons[-1].grid(row=keygrid[0], column=keygrid[1])
            elif b == 0:
                self.buttons.append(Button(self.numeric_keys_frame, text=',', width=6, height=3, padx=4, pady=4, command=lambda char='decimal': self.button_action(self.display, char)))
                self.buttons[-1].grid(row=keygrid[0], column=keygrid[1])
            else:
                self.buttons.append(Button(self.numeric_keys_frame, text=str(b), width=6, height=3, padx=4, pady=4, command=lambda char=str(b): self.button_action(self.display, char)))
                self.buttons[-1].grid(row=keygrid[0], column=keygrid[1])

            if keygrid[1] == 2:
                keygrid[0] -= 1
                keygrid[1] = 0
            else:
                keygrid[1] += 1
    
    def button_action(self, master: Misc, text: str):
        is_decimal: bool = master['text'].find('.') >= 0
        if len(master['text']) < 12 or text == '-2':
            if text == '-2':
                if is_decimal:
                    master['text'] = str(Decimal(master['text']) * Decimal('-1'))
                else:
                    master['text'] = str(int(master['text']) * -1)
            elif text == 'decimal':
                if not is_decimal:
                    master['text'] += '.'
            elif master['text'] == '0':
                master['text'] = text
            else:
                master['text'] += text

test = Application()
test.mainloop()
