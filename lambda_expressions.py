x = lambda a, b : a * b
print(x(5, 6))

def func1(n):
  return lambda a : a * n

value1 = func1(2)   # double the value
value2 = func2(3)   # tripple the value

print(value1(10))
print(value2(10))