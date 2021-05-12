a = int(input("Please, enter the first number (a): "))
b = int(input("Please, enter the second number (b): "))
# The method #1: assigning results to other variables with following output
c = a + b
d = a - b
e = a * b
f = a / b
g = a ** b
print("The results of calculations, using method #1, are: ")
print("a + b = ", c)
print("a - b = ", d)
print("a * b = ", e)
print("a / b = ", f)
print("a ** b = ", g)
# The method #2: without assigning results to the variable
print("The results of calculations, using method #2, are: ")
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a ** b = ", a ** b)