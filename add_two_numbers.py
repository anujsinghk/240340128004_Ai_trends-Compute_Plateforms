def add_two_numbers(a, b):
  """
  This function takes two numbers as input and returns their sum.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The sum of a and b.
  """
  return a + b




if __name__=='__main__':
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    sum = add_two_numbers(a, b)
    print(f"Addition of {a} and {b} : {sum}")




