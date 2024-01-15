# Regular Dictionary

user_dict = {
    "Name":"Ramesh",
    "Age":23,
    "Work":"Developer",
}

print(user_dict)

# Nested Dictionary
# we can nest lists and dictionaries in a single dictionary under nesting
nested_dict = {
    "User_data":{"Name":"Ramesh",
                 "Age" : 24,
                 "Role":"Developer",
                 "Languages":["c","c++","Java","Python","R"]}
}

print(nested_dict["User_data"])
