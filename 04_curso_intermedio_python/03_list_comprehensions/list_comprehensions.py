#squares = []

#for x in range(1,101):
#    if x %3 != 0:
#        squares.append(x**2)

squares = [x**2 for x in range(1,101) if x%3 != 0]

print(squares)