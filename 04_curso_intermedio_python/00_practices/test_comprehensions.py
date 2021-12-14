#lambda
v_multi = lambda a, b: a * b
print(v_multi(2,3))


#list comprehensions
square_pair = [i**2 for i in range(1,101) if i%2 == 0]
print(square_pair) 

#for i in squares_pair:
#    print(i)

#dicts comprehensions
squares = {i: i**2 for i in range(1,101)}
print(squares)

#for key, value in squares.items(): 
#    print(key," : ", value)

