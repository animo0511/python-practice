# Create an empty dictionay
# Allow 4 friends to entre their fav language as values and use key as their names
# Assumes that the names are unique

lan1 = input("Mahesh's fav lamguage:")
lan2 = input("Prashant's fav language:")
lan3 = input("Prathamesh's fav language:")
lan4 = input("Adarsh's fav language:")
lan5 = input("Parth's fav langauge:")


friends = {
    "Mahesh" : lan1,
    "Prashant" : lan2,
    "Prathamesh" : lan3,
    "Adarsh" : lan4,# If there is repretition of values they will be counted as separate
    "Adarsh" : lan5 # If there is repetition of keys they will be they counted as a one
}    

print(friends)