import math

class Math:
    def add(self, a: float, b: float) -> float: return a + b
    def subtract(self, a: float, b: float) -> float: return a - b
    def divide(self, a: float, b: float) -> float: return a / b
    def multiply(self, a: float, b: float) -> float: return a * b
    def gcd(self, a: float, b: float) -> float: return math.gcd(a, b)
    def area_circle(self, r: float) -> float: return math.pi * r ** 2
    def circumference(self, d: float) -> float: return math.pi * 2 * d

def main():
    calc = Math()
    print(calc.add(1, 2))
    print(calc.subtract(9,7))
    print(calc.divide(9,7))
    print(calc.multiply(9,7))
    print(calc.gcd(9,7))
    print(calc.area_circle(9))
    print(calc.circumference(9))

main()