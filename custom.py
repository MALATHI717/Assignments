class NegativeValueError(Exception):
    def __init__(self, a="Negative values are not allowed"):
        self.a = a 
        super().__init__(self.a)

def number(Num):
    if Num < 0:
        raise NegativeValueError("Enter the negative number")

try:
    number(-23)
except NegativeValueError as e:
    print(f"Custom Exception Caught: {e}")
