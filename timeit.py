import time

def calculate_time(func):
  def wrapper():
    start = time.time()
    func()
    finish = time.time()
    x = finish - start
    print("Total time " + str(x))
  return wrapper

@calculate_time
def check_Time():
  for i in range(7):
   print(i)

check_Time()
