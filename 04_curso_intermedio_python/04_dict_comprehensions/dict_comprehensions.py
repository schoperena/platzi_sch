#my_dict = {}

#for x in range(1, 101):
#    if x%3 != 0:
#        my_dict[x] = x**3

my_dict={i: i**3 for i in range(1,101) if i%3 != 0}
print(my_dict)