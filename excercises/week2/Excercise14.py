
from functools import reduce

def calc(source: list) -> int:
    return reduce(lambda x, y: x * y, source)

def maxValue(source: list) -> int:
    return max(source)

def main():
    print(calc([1, 2, 3, 4, 5]))    
    print(maxValue([1, 2, 3, 4, 5]))
main()