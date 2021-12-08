#my_list = [x for x in range(1,10000) if x%4 == 0 and x%6 == 0 and x%9 ==0]
my_list = [x for x in range(1,10000) if x%36 == 0]
print(my_list)