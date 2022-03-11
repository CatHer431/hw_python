def func_counter(func):
 def wrapper(y):
  wrapper.counter = wrapper.counter + 1
  func(y)
 wrapper.counter = 0
 return wrapper



@func_counter
def foo(y):
    return y+2**3-34

foo(3)
foo(7)
print(foo.counter) # expect 2 as output
