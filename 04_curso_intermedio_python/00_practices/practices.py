FAMILY = [
    {
        "name": "Sebastian",
        "age": 24,
        "gender": "male",
        "height": 177,
    },
    {
        "name": "Dunnys",
        "age": 23,
        "gender": "female",
        "height": 159,
    },
    {
        "name": "Ramiro",
        "age": 61,
        "gender": "male",
        "height": 170,
    },
    {
        "name": "Nora",
        "age": 56,
        "gender": "female",
        "height": 177,
    },
    {
        "name": "Ramiro A",
        "age": 36,
        "gender": "male",
        "height": 175,
    },
    {
        "name": "Raito",
        "age": 1,
        "gender": "male",
        "height": 75,
    },
    {
        "name": "Ana",
        "age": 34,
        "gender": "female",
        "height": 160,
    },
]

def main():
    #filterd by males with comprehensions
    males =[male["name"] for male in FAMILY if male["gender"] == "male"]
    print("Males in family: ", males)

    #Filtered by females with lambda and high order functions
    females = list(filter(lambda female: female["gender"] == "female", FAMILY))
    females = list(map(lambda female: female["name"], females))
    print("Females in Family: ", females)

    #Filtered by under_age with comprehensions
    under_age = [under["name"] for under in FAMILY if under["age"] < 18]
    print("under age in family: ", under_age)

    #Filtered by Adults with lambda and high order functions
    adults = list(filter(lambda adult: adult["age"] >= 18, FAMILY))
    adults = list(map(lambda adult: adult["name"], adults))
    print("Adults in family", adults)

if __name__ == "__main__":
    main()