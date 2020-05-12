from num import (

  square,
  cube
)
def three():
  print(square(3))
  print(cube(3))

def four():
  print(square(4))
  print(cube(4))

def five():
  print(square(5))
  print(cube(5))


def run(function_name):
 if function_name == "all":
   three()
   four()
   five()
 elif function_name == "three":
   three()
 elif function_name == "four":
   four()
 elif function_name == "five":
   five()
