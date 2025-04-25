class Wektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): return Wektor(self.x + other.x, self.y + other.y)
    def __sub__(self, other): return Wektor(self.x - other.x, self.y - other.y)
    def __mul__(self, other): return Wektor(self.x * other.x, self.y * other.y)  # Hadamard
    def __str__(self): return f"Wektor({self.x}, {self.y})"

w = Wektor(3, 4)
print(w)
