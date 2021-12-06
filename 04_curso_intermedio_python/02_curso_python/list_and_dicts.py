my_list = [1, "hello", True, 4.6]
my_dict = {"firstname": "Sebastian", "lastname": "Choperena"}

super_list = [
    {"firstname": "Sebastian", "lastname": "Choperena"},
    {"firstname": "Sofia", "lastname": "Garcia"},
    {"firstname": "Juan", "lastname": "Perez"},
    {"firstname": "Orlando", "lastname": "Cabrera"},
]

super_dict = {
    "natural_nums": [1,2,3,4,5],
    "integer_nums": [-2,-1,0,1,2],
    "floating_nums": [3.4,5.6,7.8],
}

for key, value in super_dict.items():
    print(key, "-", value)

for x in super_list:
    for key, value in x.items():
        print(key, "-", value)