import time

def calculate_time(func):
  def wrapper():
    start = time.time()
    func()
    runTime = time.time() - start 
    print("Run Time: " + str(runTime))
  return wrapper

@calculate_time
def check_Time():
  for i in range(7):
   print(i)

check_Time()
